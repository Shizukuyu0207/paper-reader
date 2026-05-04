#!/usr/bin/env python3
"""
Paper Fetcher — Unified PDF/content acquisition for paper-reader skill.
Tier 1: Jina Reader (fast, Markdown output)
Tier 2: Scrapling StealthyFetcher (stealth browser, raw HTML)
Tier 3: web_search fallback (metadata only)

Usage:
    python fetch_paper.py <url_or_doi> [--output-dir /tmp/paper-reader/test]
    
Output:
    - paper.md (full text in Markdown)
    - metadata.json (source, method used, char count, sections found)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time


def fetch_jina_reader(url: str, timeout: int = 30) -> dict:
    """Tier 1: Jina Reader — URL to Markdown via r.jina.ai"""
    result = {"method": "jina_reader", "success": False, "content": "", "chars": 0, "time_s": 0}
    jina_url = f"https://r.jina.ai/{url}"
    
    start = time.time()
    try:
        proc = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), jina_url, "-H", "Accept: text/plain"],
            capture_output=True, text=True, timeout=timeout + 5
        )
        elapsed = time.time() - start
        result["time_s"] = round(elapsed, 2)
        
        if proc.returncode == 0 and len(proc.stdout) > 500:
            result["success"] = True
            result["content"] = proc.stdout
            result["chars"] = len(proc.stdout)
            # Check for key sections
            for section in ["Abstract", "Results", "Methods", "Discussion", "References"]:
                result[f"has_{section.lower()}"] = section in proc.stdout
        else:
            result["error"] = f"Short response ({len(proc.stdout)} chars)" if proc.returncode == 0 else f"curl exit {proc.returncode}"
    except subprocess.TimeoutExpired:
        result["time_s"] = timeout
        result["error"] = "Timeout"
    except Exception as e:
        result["error"] = str(e)
    
    return result


def fetch_scrapling(url: str, timeout: int = 20) -> dict:
    """Tier 2: Scrapling StealthyFetcher — stealth browser fetch"""
    result = {"method": "scrapling", "success": False, "content": "", "chars": 0, "time_s": 0}
    
    try:
        from scrapling import StealthyFetcher
    except ImportError:
        result["error"] = "Scrapling not installed"
        return result
    
    start = time.time()
    try:
        page = StealthyFetcher.fetch(url, headless=True, timeout=timeout * 1000)
        elapsed = time.time() - start
        result["time_s"] = round(elapsed, 2)
        
        text = page.get_all_text() if hasattr(page, "get_all_text") else ""
        if len(text) > 500:
            result["success"] = True
            result["content"] = text
            result["chars"] = len(text)
            for section in ["Abstract", "Results", "Methods", "Discussion", "References"]:
                result[f"has_{section.lower()}"] = section in text
        else:
            result["error"] = f"Short response ({len(text)} chars)"
    except Exception as e:
        result["error"] = str(e)
    
    return result


def classify_url(url: str) -> str:
    """Classify the source type"""
    if "arxiv.org" in url:
        return "arxiv"
    elif "biorxiv.org" in url or "medrxiv.org" in url:
        return "biorxiv"
    elif "nature.com" in url:
        return "nature"
    elif "sciencedirect.com" in url or "elsevier" in url:
        return "elsevier"
    elif "doi.org" in url or url.startswith("10."):
        return "doi"
    elif url.endswith(".pdf"):
        return "pdf_direct"
    else:
        return "unknown"


def fetch_paper(url: str, output_dir: str) -> dict:
    """
    Main fetch logic: try tiers in order, return best result.
    """
    source = classify_url(url)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🔍 Fetching: {url}")
    print(f"   Source type: {source}")
    
    results = []
    
    # Tier 1: Always try Jina Reader first
    print("   Tier 1: Jina Reader...", end=" ", flush=True)
    r1 = fetch_jina_reader(url)
    print(f"{'✅' if r1['success'] else '❌'} {r1.get('chars', 0):,} chars in {r1.get('time_s', 0)}s")
    results.append(r1)
    
    # Decide if Tier 2 needed
    need_tier2 = not r1["success"]
    # Also try Tier 2 if Jina got content but missing key sections
    if r1["success"] and source == "nature":
        if not r1.get("has_methods", False) or not r1.get("has_results", False):
            need_tier2 = True
            print("   ⚠️ Jina partial (missing sections), trying Scrapling...")
    
    # Tier 2: Scrapling
    if need_tier2:
        print("   Tier 2: Scrapling StealthyFetcher...", end=" ", flush=True)
        r2 = fetch_scrapling(url)
        print(f"{'✅' if r2['success'] else '❌'} {r2.get('chars', 0):,} chars in {r2.get('time_s', 0)}s")
        results.append(r2)
    
    # Pick best result
    best = max(results, key=lambda r: r.get("chars", 0) if r["success"] else 0)
    
    if best["success"]:
        # Save content
        content_path = os.path.join(output_dir, "paper.md")
        with open(content_path, "w") as f:
            f.write(best["content"])
        
        # Save metadata
        meta = {
            "url": url,
            "source": source,
            "method": best["method"],
            "chars": best["chars"],
            "time_s": best.get("time_s", 0),
            "sections": {k.replace("has_", ""): v for k, v in best.items() if k.startswith("has_")},
        }
        meta_path = os.path.join(output_dir, "metadata.json")
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=2)
        
        print(f"\n✅ Saved: {content_path}")
        print(f"   Method: {best['method']} | {best['chars']:,} chars | {best.get('time_s', 0)}s")
        print(f"   Sections: {meta['sections']}")
        return meta
    else:
        print(f"\n❌ All tiers failed. Sources tried: {[r['method'] for r in results]}")
        for r in results:
            print(f"   {r['method']}: {r.get('error', 'unknown error')}")
        print(f"   → Fall to web_search for metadata")
        return {"method": "web_search_fallback", "source": source}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch academic paper content")
    parser.add_argument("url", help="Paper URL or DOI")
    parser.add_argument("--output-dir", default="/tmp/paper-reader/fetch_test", help="Output directory")
    args = parser.parse_args()
    
    # Normalize DOI
    url = args.url
    if re.match(r"^10\.\d{4}/", url):
        url = f"https://doi.org/{url}"
    
    fetch_paper(url, args.output_dir)
