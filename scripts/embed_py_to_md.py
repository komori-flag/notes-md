"""将 scripts/py_src/ 下的 Python 源码嵌入到 docs 中对应的 Markdown 文档

源码刻意放在 docs/ 之外：docs/ 下的任何文件都会被 mkdocs 原样复制到站点，
.py 放进去就会被公开访问。

用法（在仓库根目录执行）：
    python scripts/embed_py_to_md.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 源码目录（不参与站点构建）
SRC_ROOT = ROOT / "scripts/py_src"
# 对应文档目录
MD_ROOT = ROOT / "docs/StudyNotes/Programme-Language/python/basic"

CHAPTER = "第三章"
py_dir = SRC_ROOT / CHAPTER
md_dir = MD_ROOT / CHAPTER

# (源码文件名, 文档文件名, 文档标题)
pairs = [
    ("07-数据类型.py", "07-数据类型.md", "数据类型概述"),
    ("08-整型类型.py", "08-整型类型.md", "整型类型"),
    ("09_浮点型.py", "09-浮点型.md", "浮点型"),
    ("10_字符串_四种定义方式.py", "10-字符串的四种定义方式.md", "字符串的四种定义方式"),
    ("11_字符串_格式化输出.py", "11-字符串的格式化输出.md", "字符串的格式化输出"),
    ("12_字符串_占位符的精度控制.py", "12-字符串占位符的精度控制.md", "字符串占位符的精度控制"),
    ("13_浮点型_占位符的精度控制.py", "13-浮点型占位符的精度控制.md", "浮点型占位符的精度控制"),
    ("14_整型_占位符的精度控制.py", "14-整型占位符的精度控制.md", "整型占位符的精度控制"),
]

descriptions = {
    "07-数据类型.md": "Python 中常见的基本数据类型包括 **整型（int）**、**浮点型（float）** 和 **字符串（str）**。可以使用 `type()` 函数查看数据的类型。",
    "08-整型类型.md": "**整型（int）** 指没有小数点的数字，可为正数、负数，也可以为 `0`。",
    "09-浮点型.md": "**浮点型（float）** 指带有小数点的数值，如 `3.14`、`2.718`。还支持科学计数法表示。",
    "10-字符串的四种定义方式.md": "**字符串（str）** 可以使用单引号、双引号、三单引号、三双引号四种方式定义。其中三引号支持跨行字符串。",
    "11-字符串的格式化输出.md": "Python 提供了多种字符串格式化输出的方式：\n\n1. **字符串拼接** — 使用 `+` 连接（需手动转换非字符串类型）\n2. **占位符 `%`** — 类似 C 语言的 `printf` 风格\n3. **`str.format()` 方法** — 使用 `{}` 占位\n4. **f-string（推荐）** — 使用 `f\"...\"` 直接嵌入变量",
    "12-字符串占位符的精度控制.md": "字符串占位符可以通过 `%{m}.{n}s` 的形式对输出进行限制：\n\n- **m** — 展示的总位数，不足补空格（正数右对齐，负数左对齐）\n- **n** — 最多输出 n 个字符，超出则截断",
    "13-浮点型占位符的精度控制.md": "浮点数占位符通过 `%{m}.{n}f` 的形式控制输出格式：\n\n- **m** — 总位数（整数位 + 小数点 + 小数位），不足补空格\n- **n** — 小数点后精度，默认 6 位，超出四舍五入",
    "14-整型占位符的精度控制.md": "整型占位符通过 `%{m}.{n}d` 的形式控制输出格式：\n\n- **m** — 展示的总位数，不足补空格（正数右对齐，负数左对齐）\n- **n** — 精度控制，位数不够用 `0` 补位，小于整数位则自动失效",
}

for py_file, md_file, title_text in pairs:
    py_path = py_dir / py_file
    md_path = md_dir / md_file

    py_content = py_path.read_text(encoding="utf-8").strip("\n")

    desc = descriptions[md_file]

    md_content = f"""# {title_text}

{desc}

```python
{py_content}
```
"""
    md_path.write_text(md_content, encoding="utf-8")
    print(f"OK: {md_file} ({len(py_content)} bytes)")

print("\nDone! All .md files updated.")
