# 示例：用 env-paper-writing 撰写 Results 段落

> 更多示例：[投稿信](cover-letter.md) · [审稿回复](response-letter.md)


## 输入（用户提供的中文要点）

> 章节：Results
> 实验：在 pH=7、25 °C 条件下，用改性生物炭吸附水中 Cd²⁺。初始浓度 50 mg/L，投加量 1 g/L。
> 结果：吸附 120 min 达到平衡，去除率 92.3%，最大吸附量 48.6 mg/g（三次平行，标准差 ±1.2）。
> 对比：未改性生物炭去除率仅 61%。

## 输出（Skill 产出，节选）

**Part 1 [LaTeX]**

```latex
Under the conditions of pH~7 and 25~$^\circ$C, the modified biochar exhibited
a markedly higher affinity for Cd\textsuperscript{2+} than the pristine biochar.
Adsorption equilibrium was reached within 120~min, and the removal efficiency
attained 92.3\% at an initial concentration of 50~mg~L\textsuperscript{-1} and
a dosage of 1~g~L\textsuperscript{-1} (Figure~\ref{fig:kinetics}). The maximum
adsorption capacity reached 48.6~mg~g\textsuperscript{-1} (standard deviation
$\pm$1.2, $n = 3$), which represents an improvement of more than 50\% relative
to the pristine biochar (61\%). These results indicate that the surface
modification substantially enhanced the uptake of Cd\textsuperscript{2+}.
```

**Part 2 [中文说明]**

- 补充了「对比 pristine biochar」的相对提升表述，强化结果对比。
- 统一单位写法（mg~L⁻¹、mg~g⁻¹）并转义 LaTeX 特殊字符（`%`、`°`）。
- 引入 `Figure~\ref{}` 占位，结果陈述不展开机理（机理留给 Discussion）。
- 标注了平行实验与标准差，符合 QA/QC 报告规范。

---

> 提示：本示例为演示 skill 行为而构造，数据非真实实验结果。
