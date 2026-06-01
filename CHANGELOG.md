# Changelog

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [0.3.0] - 2026-06-02

### Added
- 新增专项 skill：`env-response-letter`（逐点审稿回复信）。
- 新增专项 skill：`env-data-availability`（数据可用性声明，含 FAIR 提示）。
- 新增 `.claude-plugin/marketplace.json`，支持 `/plugin marketplace add` 一键安装。

### Changed
- 升级 `README.md` 功能矩阵（4 → 6 个 skill）与安装说明。
- 更新主 skill 描述与插件版本号至 0.3.0。

## [0.2.0] - 2026-06-02

### Added
- 新增专项 skill：`env-abstract`（摘要 + 图文摘要要点）。
- 新增专项 skill：`env-fig-caption`（图/表标题规范）。
- 新增专项 skill：`env-cover-letter`（投稿信）。
- 新增 Claude 插件清单 `.claude-plugin/plugin.json`，支持作为插件安装。
- 新增 `examples/` 示例、`CONTRIBUTING.md` 贡献指南、`CHANGELOG.md`。
- 新增 `scripts/validate_skills.py` 校验脚本与 GitHub Actions CI。

### Changed
- 完善 `env-paper-writing` 主 skill 的描述，关联配套专项 skill。
- 升级 `README.md`，补充功能矩阵、安装方式与使用示例。

## [0.1.0] - 2026-06-01

### Added
- 初始版本：`env-paper-writing` 主 skill、README、MIT LICENSE、.gitignore。
