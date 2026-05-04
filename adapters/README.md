# Paper Reader — Multi-Agent Adapter Guide

This directory contains adapter files for using Paper Reader with different AI coding agents.

## Adapter Status

| Agent | Adapter File | Install Method | Status |
|-------|-------------|----------------|--------|
| **Hermes** | `../SKILL.md` | `~/.hermes/skills/paper-reader/` | ✅ Full support (native) |
| **Claude Code** | `claude-code/commands/paper-reader.md` | `~/.claude/commands/paper-reader.md` | ✅ Tested — full pipeline |
| **Codex** | `codex/AGENTS.md` | Project root `AGENTS.md` | ✅ Config loaded |
| **OpenCode** | `opencode/agent-config.json` | `opencode.json` agent section | ✅ Config loaded |

## Quick Install

### Claude Code

```bash
# Option 1: Copy the command file
mkdir -p ~/.claude/commands
cp adapters/claude-code/commands/paper-reader.md ~/.claude/commands/

# Verify
claude skills | grep paper-reader

# Use
# /paper-reader https://arxiv.org/abs/2604.18559
```

### Codex (OpenAI)

```bash
# Option 1: Project-level (recommended)
cp adapters/codex/AGENTS.md ./AGENTS.md
# Or append to existing AGENTS.md

# Option 2: Global
cp adapters/codex/AGENTS.md ~/.codex/AGENTS.md

# Use (in the project directory with AGENTS.md)
codex "Read this paper: https://arxiv.org/abs/2604.18559"
```

### OpenCode

```json
// Add to your opencode.json (project-level or ~/.config/opencode/)
{
  "agent": {
    "paper-reader": {
      "model": "your-model",
      "prompt": "...(see adapters/opencode/agent-config.json for full prompt)..."
    }
  }
}
```

```bash
# Use
opencode run --agent paper-reader "Read this paper: https://arxiv.org/abs/2604.18559"
```

## Feature Parity

| Feature | Hermes | Claude Code | Codex | OpenCode |
|---------|--------|-------------|-------|----------|
| 3-Tier Fetch (Jina/Scrapling/web) | ✅ Built-in | ✅ Via bash | ✅ Via bash | ✅ Via bash |
| Domain Detection (5 domains) | ✅ Native | ✅ Prompt-based | ✅ Prompt-based | ✅ Prompt-based |
| Quick Scan | ✅ | ✅ | ✅ | ✅ |
| Deep Read + Archive | ✅ | ✅ | ✅ | ✅ |
| Q&A Mode | ✅ Native | ✅ Interactive | ✅ Interactive | ✅ Interactive |
| Batch Mode (parallel) | ✅ Built-in | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual |
| MinerU Integration | ✅ Full | ✅ Via bash | ✅ Via bash | ✅ Via bash |
| Obsidian Archive | ✅ Template | ✅ Via prompt | ✅ Via prompt | ✅ Via prompt |
| Vision (figures) | ✅ Built-in | ✅ Built-in | ❌ No vision | ❌ No vision |
| Scrapling Stealth Fetch | ✅ Built-in | ⚠️ Manual install | ⚠️ Manual install | ⚠️ Manual install |

## Differences Between Agents

### Hermes (Recommended)
- **Native skill system**: SKILL.md + references/ + scripts/ auto-loaded
- **Full tool integration**: vision_analyze, web_search, execute_code all available
- **Batch mode**: Built-in parallel processing via execute_code
- **Progressive loading**: Domain checklists loaded on-demand

### Claude Code
- **Slash command**: `/paper-reader <input>` invokes the full pipeline
- **Full tool access**: Bash, Read, Write, Vision all available
- **Interactive**: Mode selection and domain confirmation work naturally
- **Best alternative to Hermes**: Closest feature parity

### Codex (OpenAI)
- **AGENTS.md**: Project-level instructions, auto-loaded from CWD
- **Bash access**: Can curl Jina Reader and run MinerU
- **No vision**: Cannot analyze figures (use captions instead)
- **TUI-only**: Must be used in interactive terminal mode

### OpenCode
- **Agent config**: Define paper-reader as a named agent in opencode.json
- **Run mode**: `opencode run --agent paper-reader "..."` for non-interactive
- **TUI-primary**: Best used in TUI mode, run mode has output capture limitations
- **Model flexibility**: Works with any configured provider

## Test Results (2026-05-04)

Test paper: [ConforNets (arXiv:2604.18559)](https://arxiv.org/abs/2604.18559)

| Agent | Method | Response Time | Correct? |
|-------|--------|--------------|----------|
| Claude Code | `/paper-reader` command, print mode | ~50s | ✅ Correct title and findings |
| Codex | AGENTS.md, TUI mode | N/A (TUI) | ✅ Config loaded, AGENTS.md read |
| OpenCode | agent config, run mode | N/A (TUI) | ✅ Config loaded, API call initiated |

### Claude Code Output (verbatim):
> **Title:** ConforNets: Latents-Based Conformational Control in OpenFold3
>
> **Main Finding:** ConforNets introduce channel-wise affine transforms of pre-Pairformer pair latents in AlphaFold3 to globally modulate conformational variability — achieving state-of-the-art success on all existing multi-state benchmarks for unsupervised alternate state generation.
