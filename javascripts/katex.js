// 数学公式渲染 (KaTeX)
// 参考: https://squidfunk.github.io/mkdocs-material/reference/math/
document$.subscribe(({ body }) => {
  renderMathInElement(body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\(", right: "\\)", display: false },
      { left: "$", right: "$", display: false },
      { left: "\\[", right: "\\]", display: true },
    ],
  });
});
