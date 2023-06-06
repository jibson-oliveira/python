import requests
import json

mensagem = { "text": "Olá, bem-vindo ao canal de testes"}
webhook = "https://hooks.slack.com/services/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"

# Postar mensagens no canal
requests.post(webhook, data=json.dumps(mensagem))