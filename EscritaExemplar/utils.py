import requests
import json

def enviar_redacao_para_correcao(redacao):
    API_KEY="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"  # Substitua pela sua chave de API do GPT-3

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": f"corrija os erros gramaticais e coesivos da redação", "role": "system"}]
    }
    body_mensagem["messages"].append({"role": "user", "content": redacao})

    body_mensagem = json.dumps(body_mensagem)

    resposta_api = requests.post(link, headers=headers, data=body_mensagem)
    if resposta_api.status_code == 200:
        resposta = resposta_api.json()
        redacao_corrigida = resposta["choices"][0]["message"]["content"]
        return redacao_corrigida
    else:
        return "Erro ao enviar a redação para correção."
