# LangBot Trigger Plugin
[LangBot](https://github.com/langbot-app/LangBot) é uma plataforma open-source para o desenvolvimento de robôs de mensagens instantâneas nativos de LLM, que visa fornecer uma experiência pronta para uso no desenvolvimento de bots de IM, com funções como Agente, RAG, MCP e outros recursos de aplicações LLM, adaptando-se a plataformas globais de mensagens instantâneas e oferecendo APIs ricas, suportando desenvolvimento personalizado.

Este plugin de trigger é utilizado para processar eventos de mensagens recebidas pelo Webhook do LangBot. Ele pode ser usado para acionar fluxos de trabalho no Dify ao receber mensagens de uma instância LangBot.

## Como usar

1. Instale este plugin no Dify.
2. Configure a instância LangBot conforme a [documentação do LangBot](https://docs.langbot.app/pt/insight/guide.html).
3. Abra a página de assinatura no Dify e copie a URL do Webhook.

![Página de Assinatura](./_assets/config_sub.png)

4. Volte à página de integração de API do LangBot, cole a URL do Webhook e salve a configuração.

![Página de Integração de API](./_assets/config_api.png)

5. Receba mensagens dos bots configurados ou teste na página de depuração de pipeline do LangBot.

![Página de Depuração de Pipeline](./_assets/pipeline_debug.png)

6. Agora você pode usar este plugin para acionar fluxos de trabalho do Dify sempre que uma mensagem de uma instância LangBot for recebida.

![Página de Fluxo de Trabalho](./_assets/workflow_debug.png)

