# 充分统计量方法学习笔记

经济学中的 sufficient statistics 方法，研究的是：**为了回答一个明确的福利或政策问题，究竟需要估计哪些量？** 在给定模型条件下，有时不必估计全部偏好和技术参数，只需识别少数行为反应、份额或财政影响。

本仓库采用中文讲解，按“问题 → 直觉 → 公式 → 数值例子 → 适用边界”展开。这里的主题是经济学中的充分统计量方法；统计学中的充分统计量会作为概念对照介绍。

## 从这里开始

第一次只有 30 分钟：读 [第 1 单元](notes/01-map-and-core-ideas.md) 和 [第 2 单元](notes/02-envelope-and-taxation.md) 的商品税例子，再做 [自测题](exercises/01-self-check.md) 第 1—4 题。其余内容按 [学习路线](learning-path.md) 逐步展开。

| 单元 | 要回答的问题 | 笔记 |
|---|---|---|
| 1 | “充分”是相对于什么而言？ | [研究地图与核心思想](notes/01-map-and-core-ideas.md) |
| 2 | 行为反应怎样变成福利变化？ | [包络定理与税收](notes/02-envelope-and-taxation.md) |
| 3 | 怎样评价保险与政府支出？ | [社会保险与公共资金边际价值](notes/03-insurance-and-mvpf.md) |
| 4 | 回归得到的系数能直接代入吗？ | [识别、推断与研究流程](notes/04-identification-and-workflow.md) |
| 5 | 为什么贸易份额能帮助计算贸易福利？ | [与国际贸易的连接](notes/05-trade-bridge.md) |

配套材料：[术语表](glossary.md)、[9 篇经典与进阶文献](classic-papers/README.md)、[练习](exercises/01-self-check.md)、[参考答案](exercises/01-answers.md)、[论文阅读模板](templates/paper-note.md)、[可运行数值例子](code/README.md)。

## 核心地图

```mermaid
flowchart LR
    A[政策问题与福利对象] --> B[经济模型与假设]
    B --> C[推导需要的统计量]
    C --> D[用数据识别统计量]
    D --> E[代入公式并传播不确定性]
    E --> F[解释适用范围和政策含义]
```

“充分”不等于“任何一个显著系数都够用”，也不意味着可以跳过模型、分配权重或因果识别。总量福利、某一群体的福利、局部改革和大幅政策变化，可能需要不同的统计量。

## 文件结构

```text
sufficient-statistics-learning/
├── README.md
├── learning-path.md
├── glossary.md
├── notes/               五个主题单元
├── classic-papers/      文献入口与阅读问题
├── exercises/           自测题与答案
├── templates/           单篇论文阅读模板
└── code/                无第三方依赖的教学计算
```

## 与其他学习仓库衔接

- [国际贸易学习](https://github.com/GuoqingOu/trade-economics-learning)：从比较优势到贸易福利、引力模型和生产网络。
- [网络经济学学习](https://github.com/GuoqingOu/network-economics-learning)：理解连接、外部性和传播；这些机制可能改变福利公式所需的统计量。

## 使用说明

直接在 GitHub 点击文件阅读，或通过 **Code → Download ZIP** 下载。数学使用 GitHub 支持的 Markdown 公式；Mermaid 图的本地显示取决于编辑器。

本仓库保存原创解释、教学例子和原文链接。数值例子均为人为设定，不是实证结果或政策建议；原始论文、课件和个人研究资料不在仓库中。第一版整理于 2026-10-05，定位为基础学习与进阶阅读入口。
