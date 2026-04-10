# agiproject

这是一个用于学习 LangChain 的 Python 项目，包含了提示词模板、结构化输出、多模型配置等常见实践。

## 项目定位

- 学习如何使用 LangChain 与不同模型服务进行交互
- 学习 Few-shot Prompt 模板的组织方式
- 学习结构化输出（Pydantic Schema）
- 学习 Python 包/模块运行方式（`python -m` 与 `uv` 脚本入口）

## 目录结构与文件功能

### 根目录

- `main.py`：项目主入口示例，演示使用 `with_structured_output` 让模型按 `Joke` 结构返回结果。
- `models.py`：统一管理模型初始化，读取 `.env` 与 `.env.local`，当前包含 GitHub Models、Qwen、DeepSeek 三个模型对象。
- `pyproject.toml`：项目配置文件，包含依赖列表、`uv`/打包配置，以及脚本命令 `structured-output`。
- `uv.lock`：`uv` 生成的锁文件，用于固定依赖版本，保证环境可复现。
- `.env.example`：环境变量模板文件（无敏感信息），用于说明需要配置哪些 Key。
- `.gitignore`：Git 忽略规则，已忽略 `.env`、`.env.local` 等本地敏感配置文件。
- `README.md`：项目说明文档（当前文件）。

### langchain_apis/

- `langchain_apis/__init__.py`：包标记文件，确保可使用模块方式运行子文件。
- `langchain_apis/fewshot_prompt_template.py`：FewShotPromptTemplate 示例，演示如何组织样例并生成最终提示词。
- `langchain_apis/structured_output/__init__.py`：`structured_output` 子包标记文件。
- `langchain_apis/structured_output/with_structured_output.py`：结构化输出示例，可通过 `uv run structured-output` 运行。
- `langchain_apis/OST.md`：运行规范说明，包含新建子目录后如何执行模块的最佳实践。

### notes/

- `notes/基础概念.md`：学习笔记，记录 LangChain 相关基础概念。

## 快速开始

1. 安装依赖

```bash
uv sync
```

2. 配置环境变量

```bash
cp .env.example .env.local
```

然后在 `.env.local` 中填入你自己的 API Key。

3. 运行示例

```bash
uv run python main.py
```

或运行结构化输出子模块：

```bash
uv run structured-output
```
