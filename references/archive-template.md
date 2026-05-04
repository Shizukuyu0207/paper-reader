# Archive Note Template (Obsidian)

## Usage
This template is filled during Mode B (Deep Read) and saved to `~/obsidian/papers/{domain}/`.
File naming: `{year}-{ShortTitleKeyword}.md`

---

```markdown
---
title: "[论文标题]"
authors: ["[第一作者]", "[通讯作者]"]
year: [年份]
journal: "[期刊/会议名]"
doi: "[DOI]"
arxiv: "[arXiv ID]"
domain: "[主领域: md/med/ai/bio/prog]"
sub_domain: "[副领域]"
date_read: "[YYYY-MM-DD]"
tags: [[领域], [方法关键词], [软件/工具]]
paper_type: "[research/review/methods/preprint]"
rating: "[1-5]"
---

# [论文标题]

## 基本信息
- **作者**: [第一作者] et al. | 通讯: [通讯作者]
- **机构**: [主要机构]
- **期刊/会议**: [名称], [年份]
- **链接**: [arXiv/DOI URL]

## 研究问题与动机
[1-3段描述论文要解决的核心问题及其研究背景]

## 方法
[领域体检表内容 — 按domain-{domain}.md逐项填写]

## 核心结果
### 主要发现
- [关键数据 + 效应量 + 具体数值]
- [发现2]
- [发现3]

### 关键图表
![[images/{fig_filename}]]
> Figure N: [图注描述]

[更多图表...]

## 局限性
- **作者自述**: [作者承认的局限]
- **补充判断**: [你自己的分析]

## 对本研究的启示
[与用户研究方向的关联 + 可借鉴之处 + 潜在应用场景]

## 引用网络
- **基于的先前工作**: [关键参考文献]
- **被引用情况**: [如可获取]

## 原文资源
- **PDF**: [本地路径或下载链接]
- **图片目录**: [images/目录路径]
- **MinerU输出**: [content_list.json路径]
```

---

## Image Handling
When generating the archive note:
1. Copy all extracted images from MinerU output to `~/obsidian/papers/{domain}/images/`
2. Rename images descriptively: `fig{N}_{description}.jpg`
3. In the note, use Obsidian wiki-link syntax: `![[images/fig1_rmsd_plot.jpg]]`
4. Include figure captions as blockquotes below each image

## Tags Format
Tags should include:
- Domain: `#paper/md` or `#paper/medicine` etc.
- Method keywords: `#molecular-dynamics`, `#fep`, `#rna-seq`
- Software: `#amber`, `#gromacs`, `#pytorch`
- Paper type: `#research` or `#review` or `#methods`
