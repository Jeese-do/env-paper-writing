# env-paper-writing

[![Validate Skills](https://github.com/1768898664-bit/env-paper-writing/actions/workflows/validate.yml/badge.svg)](https://github.com/1768898664-bit/env-paper-writing/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一组面向**环境学科（环境科学 / 环境工程）英文学术论文写作**的 [Claude](https://claude.com/claude-code) Skills 合集。

它帮助你撰写、润色与梳理环境领域 SCI 论文的各个部分，输出符合期刊出版标准、语言严谨、逻辑清晰的学术英文文本——从整篇章节写作，到摘要、图表标题、投稿信等专项场景。

## ✨ 包含的 Skills

| Skill | 用途 | 适用场景 |
| --- | --- | --- |
| [`env-paper-writing`](skills/env-paper-writing/SKILL.md) | 通用分章节论文写作与润色 | 撰写/改写 Abstract、Introduction、Methods、Results、Discussion、Conclusion |
| [`env-abstract`](skills/env-abstract/SKILL.md) | 摘要专项 | 生成结构完整、含定量结果的英文摘要 + 关键词 + 图文摘要要点 |
| [`env-fig-caption`](skills/env-fig-caption/SKILL.md) | 图/表标题 | 把中文描述转为规范英文 Figure / Table caption |
| [`env-cover-letter`](skills/env-cover-letter/SKILL.md) | 投稿信 | 撰写突出创新点与期刊契合度的英文 Cover Letter |

## 🎯 设计特点

- 📑 **分章节写作指导**：针对各章节给出写作逻辑与要点。
- 🧪 **环境学科术语规范**：准确使用领域术语与单位（COD、BOD、PM2.5、mg L⁻¹、μg m⁻³）。
- ✍️ **SCI 期刊级语言润色**：提升严谨性、清晰度与可读性，杜绝非母语生硬表达。
- 📐 **LaTeX 友好**：保留 `\cite{}`、`\ref{}`、数学公式等命令，自动转义特殊字符。
- 🌍 **环境意义导向**：强调研究的环境意义（environmental implications）与应用价值。
- 🛡️ **科学严谨**：不编造数据、不夸大结论，缺失信息以占位符提示补充。

## 📦 安装与使用

### 方式一：作为单个 Skill 使用

将任一 skill 目录复制到你的 Claude skills 目录下：

```
~/.claude/skills/env-paper-writing/SKILL.md
```

然后在 Claude Code 中通过 `/env-paper-writing` 调用，或直接描述写作需求自动触发。

### 方式二：作为 Claude 插件安装（推荐）

本仓库自带 `.claude-plugin/plugin.json`，可作为插件整体安装，一次获得全部 skills：

```bash
git clone https://github.com/1768898664-bit/env-paper-writing.git
```

将其加入你的 Claude 插件 marketplace 后即可使用全部四个 skill。

## 🧪 使用示例

> 帮我把这段中文实验结果改写为环境 SCI 论文的 Results 段落：在 pH=7 条件下，改性生物炭对 Cd²⁺ 的去除率达到 92.3%，最大吸附量 48.6 mg/g。

Skill 将输出规范的英文 LaTeX 文本，并附中文修改说明。

👉 完整示例见 [`examples/results-paragraph.md`](examples/results-paragraph.md)。

## 🗂️ 目录结构

```
env-paper-writing/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .claude-plugin/
│   └── plugin.json
├── .github/workflows/
│   └── validate.yml
├── scripts/
│   └── validate_skills.py
├── examples/
│   └── results-paragraph.md
└── skills/
    ├── env-paper-writing/SKILL.md
    ├── env-abstract/SKILL.md
    ├── env-fig-caption/SKILL.md
    └── env-cover-letter/SKILL.md
```

## 🤝 贡献

欢迎提 Issue 或 PR 来完善章节指导、术语库与写作规范。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并在提交前运行：

```bash
python scripts/validate_skills.py
```

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源。

---

> ⚠️ 免责声明：本工具用于辅助学术写作（语言润色、结构梳理、规范化表达），不替代作者对研究内容、数据真实性与学术诚信的责任。请遵守目标期刊关于 AI 辅助写作的披露政策。
