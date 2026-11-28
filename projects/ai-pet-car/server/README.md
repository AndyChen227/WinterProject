<sub>[🏠 首页](../../../README.md) › [🛠️ 项目](../../README.md) › [🐱 AI 电子宠物小车](../README.md) › ☁️ 电脑上的 AI 服务</sub>

<img src="../media/art/mascot-think.svg" width="90" align="right">

# ☁️ server · 电脑上的 AI 服务

> 一个 Python 小服务：听懂小车传来的话，把回答和动作指令发回去。

| 📍 状态 | 📝 对应的开发计划 |
| :-: | --- |
| 还没开始 | [板块 6 · AI 大脑（服务端）](../docs/PLAN.md#m6) |

## 🔄 它做的事

```mermaid
flowchart LR
    A["🎤 小车传来的语音"] --> B["语音识别"] --> C["大模型<br>DeepSeek / Claude"] --> D["语音合成"] --> E["🐱 回答和动作指令<br>发回小车"]
    style A fill:#FFF1F5,stroke:#C2456E,color:#5B4A42
    style E fill:#FFF1F5,stroke:#C2456E,color:#5B4A42
    style B fill:#EAF6FF,stroke:#3A7BD5,color:#5B4A42
    style C fill:#EAF6FF,stroke:#3A7BD5,color:#5B4A42
    style D fill:#EAF6FF,stroke:#3A7BD5,color:#5B4A42
```

收到小车传来的语音 → 语音识别 → 大模型（DeepSeek / Claude）→ 语音合成，把回答和动作指令发回小车。

---

<p align="center"><sub><a href="../firmware">← 💾 小车上的程序</a> &nbsp;·&nbsp; <a href="../README.md">🐱 项目首页</a></sub></p>
