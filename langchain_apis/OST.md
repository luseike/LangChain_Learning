# langchain_apis 运行 OST 说明

## 1. 目录与文件规范

在 `langchain_apis` 下新建目录时，建议结构如下：

```text
langchain_apis/
  new_topic/
    __init__.py
    demo.py
```

注意：
- 新目录里建议加 `__init__.py`，确保是标准 Python 包。
- Python 文件里建议提供 `main()` 入口，并加上：

```python
if __name__ == "__main__":
    main()
```

## 2. 推荐运行方式（通用）

在项目根目录执行：

```bash
uv run python -m langchain_apis.new_topic.demo
```

规则：
- `-m` 后写模块路径，不写 `.py`
- 用点号连接目录和文件名
- 必须从项目根目录运行

示例：
- 文件路径：`langchain_apis/new_topic/demo.py`
- 运行命令：`uv run python -m langchain_apis.new_topic.demo`

## 3. 常见错误与修复

### 错误 1：把 `.py` 写到 `-m` 后面

错误示例：

```bash
uv run -m langchain_apis.new_topic.demo.py
```

修复：

```bash
uv run python -m langchain_apis.new_topic.demo
```

### 错误 2：ModuleNotFoundError

排查顺序：
1. 是否在项目根目录执行命令。
2. 新目录是否有 `__init__.py`。
3. 依赖是否已安装：`uv sync`。

## 4. 可选：配置短命令

如果你希望像 `uv run structured-output` 这样短命令运行，可在 `pyproject.toml` 的 `[project.scripts]` 增加：

```toml
[project.scripts]
new-topic-demo = "langchain_apis.new_topic.demo:main"
```

然后执行：

```bash
uv sync
uv run new-topic-demo
```

## 5. 快速模板

新建文件后可直接用这个最小模板：

```python
def main() -> None:
    print("hello from new module")


if __name__ == "__main__":
    main()
```
