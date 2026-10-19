"""把 scripts/py_src/ 下的 Python 源码同步进 docs 中对应的 Markdown 文档

源码刻意放在 docs/ 之外：docs/ 下的任何文件都会被 mkdocs 原样复制到站点，
.py 放进去就会被公开访问。

两种同步方式，由 Markdown 里的标记行决定（标记用引用式链接定义 `[//]: # (...)` 的
惯用写法，渲染时整行消失，不会像 HTML 注释那样残留在页面和搜索结果里）：

1. 整文件模式 —— 标记 `[//]: # (py)`
   .py 的全部内容替换标记后面那个代码块的正文。
   适合「标题 + 说明 + 一个完整示例」的文档（07~14）。

2. 片段模式 —— 标记 `[//]: # (py: 片段名)`
   用 .py 里 `# @snippet 片段名` ... `# @end` 之间的内容替换代码块正文。
   适合夹叙夹议、多个代码块的文档（01~03）。讲解文字不受影响，只刷新代码。

标记与代码块之间的空行、以及代码块的缩进（折叠框内）都会原样保留。

用法（可在任意目录执行）：
    python scripts/embed_py_to_md.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

SRC_ROOT = ROOT / "scripts/py_src"          # 源码目录（不参与站点构建）
MD_ROOT = ROOT / "docs/StudyNotes/Programme-Language/python/basic"

CHAPTER = "第三章"
py_dir = SRC_ROOT / CHAPTER
md_dir = MD_ROOT / CHAPTER

# ---- 整文件模式：(源码, 文档) ----
# 文档的标题和说明写在 .md 里手工维护，脚本只刷新标记后面的代码块
WHOLE_FILE = [
    ("07-数据类型.py", "07-数据类型.md"),
    ("08-整型类型.py", "08-整型类型.md"),
    ("09_浮点型.py", "09-浮点型.md"),
    ("10_字符串_四种定义方式.py", "10-字符串的四种定义方式.md"),
    ("11_字符串_格式化输出.py", "11-字符串的格式化输出.md"),
    ("12_字符串_占位符的精度控制.py", "12-字符串占位符的精度控制.md"),
    ("13_浮点型_占位符的精度控制.py", "13-浮点型占位符的精度控制.md"),
    ("14_整型_占位符的精度控制.py", "14-整型占位符的精度控制.md"),
]

# ---- 片段模式：(源码, 文档) ----
SNIPPET_FILES = [
    ("01-字面量.py", "01-字面量.md"),
    ("02-变量.py", "02-变量.md"),
    ("03-标识符.py", "03-标识符.md"),
    # 04-常量.md 目前只有标题，等正文写好后补进来
]

WHOLE_RE = re.compile(r"^(\s*)\[//\]:\s*#\s*\(\s*py\s*\)\s*$")
SNIPPET_RE = re.compile(r"^(\s*)\[//\]:\s*#\s*\(\s*py:\s*([\w.-]+)\s*\)\s*$")
SNIPPET_DEF_RE = re.compile(r"^#\s*@snippet\s+([\w.-]+)\s*$")


class EmbedError(Exception):
    pass


def read_lines(path):
    return path.read_text(encoding="utf-8").split("\n")


def extract_snippet(py_lines, name, py_name):
    """取出 # @snippet name ... # @end 之间的正文（去掉块尾空行）"""
    start = None
    for i, ln in enumerate(py_lines):
        m = SNIPPET_DEF_RE.match(ln)
        if m and m.group(1) == name:
            start = i + 1
            break
    if start is None:
        raise EmbedError(f"{py_name}: 找不到片段 {name}")
    end = None
    for i in range(start, len(py_lines)):
        if py_lines[i].strip() == "# @end":
            end = i
            break
    if end is None:
        raise EmbedError(f"{py_name}: 片段 {name} 缺少 # @end")
    body = py_lines[start:end]
    while body and not body[-1].strip():
        body.pop()
    return body


def replace_block_body(md_lines, marker_idx, body_lines, md_name, mode_desc):
    """把 marker_idx 之后第一个代码块的正文换成 body_lines，保留缩进"""
    open_idx = None
    for i in range(marker_idx + 1, len(md_lines)):
        if md_lines[i].strip().startswith("```"):
            open_idx = i
            break
        if md_lines[i].strip():
            raise EmbedError(f"{md_name}: {mode_desc} 标记后不是代码块")
    if open_idx is None:
        raise EmbedError(f"{md_name}: {mode_desc} 标记后找不到代码块")

    close_idx = None
    for i in range(open_idx + 1, len(md_lines)):
        if md_lines[i].strip().startswith("```"):
            close_idx = i
            break
    if close_idx is None:
        raise EmbedError(f"{md_name}: {mode_desc} 的代码块未闭合")

    fence_indent = md_lines[open_idx][: len(md_lines[open_idx]) - len(md_lines[open_idx].lstrip())]
    new_body = [(fence_indent + ln) if ln.strip() else "" for ln in body_lines]
    md_lines[open_idx + 1:close_idx] = new_body
    return open_idx, len(new_body)


def sync_whole_file(py_name, md_name):
    py_lines = read_lines(py_dir / py_name)
    md_path = md_dir / md_name
    md_lines = read_lines(md_path)

    hits = [i for i, ln in enumerate(md_lines) if WHOLE_RE.match(ln)]
    if len(hits) != 1:
        raise EmbedError(f"{md_name}: 期望 1 个 <!-- py --> 标记，实际 {len(hits)} 个")

    body = list(py_lines)
    while body and not body[-1].strip():
        body.pop()
    replace_block_body(md_lines, hits[0], body, md_name, "整文件")
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    return f"整文件 {py_name} -> {md_name}（{len(body)} 行）"


def sync_snippet_file(py_name, md_name):
    py_lines = read_lines(py_dir / py_name)
    md_path = md_dir / md_name
    md_lines = read_lines(md_path)

    hits = [(i, m) for i, ln in enumerate(md_lines) if (m := SNIPPET_RE.match(ln))]
    if not hits:
        raise EmbedError(f"{md_name}: 找不到 <!-- py: 片段名 --> 标记")

    done = []
    for idx, m in reversed(hits):          # 从后往前改，行号不失效
        name = m.group(2)
        body = extract_snippet(py_lines, name, py_name)
        _, n = replace_block_body(md_lines, idx, body, md_name, f"片段 {name}")
        done.append(f"{name}({n} 行)")

    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    return f"片段 {py_name} -> {md_name}：{'、'.join(reversed(done))}"


def main():
    failures = []
    for py_name, md_name in WHOLE_FILE:
        if not (py_dir / py_name).exists():
            failures.append(f"{py_name}: 源码不存在")
            continue
        if not (md_dir / md_name).exists():
            failures.append(f"{md_name}: 文档不存在")
            continue
        try:
            print("OK: " + sync_whole_file(py_name, md_name))
        except EmbedError as e:
            failures.append(str(e))

    for py_name, md_name in SNIPPET_FILES:
        try:
            print("OK: " + sync_snippet_file(py_name, md_name))
        except EmbedError as e:
            failures.append(str(e))

    if failures:
        print("\n失败：", file=sys.stderr)
        for f in failures:
            print("  - " + f, file=sys.stderr)
        return 1

    print("\nDone! All .md files updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
