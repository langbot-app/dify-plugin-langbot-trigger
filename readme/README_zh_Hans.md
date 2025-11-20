# LangBot Trigger Plugin

[LangBot](https://github.com/langbot-app/LangBot) 是一个开源的 LLM 原生即时通讯机器人开发平台，旨在提供开箱即用的 IM 机器人开发体验，具备 Agent、RAG、MCP 等 LLM 应用功能，适应全球即时通讯平台，提供丰富的 API 接口，支持定制开发。

本触发器插件用于处理 LangBot Webhook 的消息事件。它可以在收到 LangBot 实例的消息时触发 Dify 工作流。

## 使用方法

1. 安装此插件到 Dify。
2. 按照 [LangBot 文档](https://docs.langbot.app/zh/insight/guide.html) 配置 LangBot 实例。
3. 在 Dify 中打开订阅页面，复制 Webhook URL。

![Subscription Page](./_assets/config_sub.png)

4. 回到 LangBot API 集成页面，填入 Webhook URL 并保存配置。

![API Integration Page](./_assets/config_api.png)

5. 收到配置的机器人消息，或测试 LangBot 流水线调试页面。

![Pipeline Debug Page](./_assets/pipeline_debug.png)

6. 现在可以使用此插件在收到 LangBot 实例的消息时触发 Dify 工作流。

![Workflow Page](./_assets/workflow_debug.png)
