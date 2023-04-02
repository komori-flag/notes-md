# MKDocs 的安装
<a href='/MKDocs/1-mkdocs-what/' target="_black">前面一章</a>提到了 MKDocs 是由 Python 进行开发的，因此安装它自然而然肯定也需要使用到 Python 。

它需要 <a href='https://www.python.org/' target="_black">Python</a> 和 Python package manager pip（通用的 Python 包管理工具） 来进行安装。

---
## 安装
使用 pip 安装:
```text
pip install mkdocs
# 或者是用pip3
pip3 install mkdocs
```

---
## 验证安装
安装完成以后可以通过查看版本来验证 MKDocs 是否安装到位
```text
mkdocs -V
mkdocs, version 1.4.2 from C:\Python\Python310\site-packages\mkdocs (Python 3.10)
```

---
## 创建新项目
安装到位后可以试着创建一个新的项目
```text
# 项目名可自拟
mkdocs new my-project
```
此时 MKDocs 便会创建并初始化项目，初始化完成后便可以在当前执行命令的目录中看到这个新创建的项目文件夹。

在新创建的项目文件夹下可以看到一个配置文件<code style='color: red'>mkdocs.yml</code>和一个包含文档源码的<code style='color: red'>docs</code>文件夹，文件夹当中包含了一个初始的<code style='color: red'>index.md</code>源码文档。
```text
# 项目文件夹目录
mkdocs.yml
docs/
    index.md
```

---
## 内置的开发服务器
MkDocs 带有一个内置的开发服务器可用来预览文档，在当前项目文件夹下使用命令即可启动。
```text
mkdocs server
Running at: http://127.0.0.1:8000/
```
内置的开发服务器可以在配置文件、文档目录或主题发生改变时自动重载并重新生成文档（出错会直接停止运行）。

此时在浏览器中便可以打开这个网址预览默认的`index.md`文档了

![](./File/2-Install/screenshot.png)
---

