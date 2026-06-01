# env-paper-writing

一个用于**环境学科（环境科学 / 环境工程）英文学术论文写作**的 Claude Skill。

它帮助你撰写、润色与梳理环境领域 SCI 论文的各个章节（摘要、引言、方法、结果、讨论、结论），输出符合期刊出版标准、语言严谨、逻辑清晰的学术英文文本。

## 功能特点

- 📑 **分章节写作指导**：针对 Abstract / Introduction / Methods / Results / Discussion / Conclusion 各章节给出写作要点。
- 🧪 **环境学科术语规范**：准确使用领域术语与单位（如 COD、BOD、PM2.5、mg L⁻¹）。
- ✍️ **学术语言润色**：提升严谨性、清晰度与可读性，符合 SCI 期刊语体。
- 📐 **LaTeX 友好**：保留 `\cite{}`、`\ref{}`、数学公式等命令，自动转义特殊字符。
- 🌍 **环境意义导向**：强调研究的环境意义（environmental implications）与应用价值。

## 安装与使用

### 作为 Claude Code Skill 使用

1. 将本仓库的 `skills/env-paper-writing/` 目录复制到你的 Claude skills 目录下，例如：

   ```
   ~/.claude/skills/env-paper-writing/SKILL.md
   ```

2. 在 Claude Code 中通过 `/env-paper-writing` 调用，或直接描述你的写作需求触发。

### 使用示例

> 帮我把这段中文实验结果改写为环境 SCI 论文的 Results 段落：在 pH=7 条件下，吸附剂对 Cd²⁺ 的去除率达到 92.3%。

Skill 将输出规范的英文 LaTeX 文本，并附中文修改说明。

## 目录结构

```
env-paper-writing/
├── README.md
├── LICENSE
└── skills/
    └── env-paper-writing/
        └── SKILL.md
```

## 贡献

欢迎提 Issue 或 PR 来完善章节指导、术语库与写作规范。

## 许可证

本项目采用 [MIT License](LICENSE) 开源。
