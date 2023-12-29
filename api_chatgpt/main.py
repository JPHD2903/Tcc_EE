from senha import API_KEY
import requests
import json

def obter_redacao_do_cliente():
    redacao = input("Digite a palavra: ")
    return redacao

def enviar_redacao_para_correcao(redacao):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/chat/completions"
    id_modelo = "gpt-3.5-turbo"

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": f"corija a frase a seguir", "role": "system"}]
    }
    body_mensagem["messages"].append({"role": "user", "content": redacao})
    
    body_mensagem = json.dumps(body_mensagem)

    requesicao = requests.post(link, headers=headers, data=body_mensagem)
    return requesicao

def main():
    redacao_cliente = obter_redacao_do_cliente()
    resposta_da_api = enviar_redacao_para_correcao(redacao_cliente)

    if resposta_da_api.status_code == 200:
        resposta = resposta_da_api.json()
        mensagem = resposta["choices"][0]["message"]["content"]
        print("Redação Corrigida:")
        print(mensagem)
    else:
        print("Alguma coisa deu errado.")

if __name__ == "__main__":
    main()

