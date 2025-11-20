# LangBot Trigger プラグイン

[LangBot](https://github.com/langbot-app/LangBot) は、オープンソースのLLMネイティブなインスタントメッセージングボット開発プラットフォームです。エージェント、RAG、MCPなどのLLMアプリケーション機能を備え、グローバルなIMプラットフォームに対応し、豊富なAPIインターフェースを提供、カスタム開発をサポートします。

このトリガープラグインは、LangBot Webhookからのメッセージイベントを処理するために使用します。LangBotインスタンスからメッセージを受信した際に、Difyのワークフローをトリガーできます。

## 使い方

1. このプラグインをDifyにインストールします。
2. [LangBotドキュメント](https://docs.langbot.app/ja/insight/guide.html) に従ってLangBotインスタンスを設定します。
3. Difyでサブスクリプションページを開き、Webhook URLをコピーします。

![Subscription Page](./_assets/config_sub.png)

4. LangBotのAPI連携ページに戻り、Webhook URLを入力して設定を保存します。

![API Integration Page](./_assets/config_api.png)

5. 設定済みボットからメッセージを受信、またはLangBotのパイプラインデバッグページでテストします。

![Pipeline Debug Page](./_assets/pipeline_debug.png)

6. これで、LangBotインスタンスからメッセージを受信すると、このプラグインでDifyワークフローをトリガーできるようになります。

![Workflow Page](./_assets/workflow_debug.png)
