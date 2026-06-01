# 贡献指南 / Contributing

感谢你愿意为 **env-paper-writing** 出一份力！本项目是一组面向环境学科论文写作的 Claude Skills，欢迎以下形式的贡献：

- 🐛 报告问题：术语错误、写作建议不当、示例有误等
- ✨ 新增 skill：针对环境领域写作的新场景（如审稿回复、数据可用性声明）
- 📚 完善文档与示例
- 🌐 改进多语言支持

## 新增或修改 Skill 的规范

每个 skill 是一个独立目录 `skills/<name>/SKILL.md`，必须包含 YAML frontmatter：

```markdown
---
name: <kebab-case 名称，需与目录名一致>
description: <一句话说明何时使用该 skill，用于触发判断>
---

# Role
...

# Task
...
```

要求：

1. `name` 必须是 kebab-case，且与所在目录名**完全一致**。
2. `description` 要清楚说明「**何时**使用」，便于自动触发，建议以使用场景结尾。
3. 正文用清晰的小节（Role / Task / Constraints / Output Format / Input）组织。
4. 保持环境学科术语与单位规范，避免编造数据。

## 提交流程

1. Fork 本仓库并新建分支：`git checkout -b feature/your-skill`
2. 添加/修改 skill，并在 `examples/` 下尽量附一个示例
3. 本地运行校验脚本：`python scripts/validate_skills.py`
4. 提交 PR，说明改动动机与适用场景

## 校验

CI 会自动运行 `scripts/validate_skills.py`，检查每个 `SKILL.md` 的 frontmatter 是否完整、`name` 是否与目录名一致。请确保本地通过后再提交。
