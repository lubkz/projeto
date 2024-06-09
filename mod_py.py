# Dicionário FAQ com palavras-chave e respostas
faq = {
    "1" : "O horário de atendimento é...",
    "2" : "O local de atendimento é na...",
    "3" : "O endereço da rua é...",
    "4" : "A empresa é especializada em...",
    "5" : "Serviços de atendimento nas regiões...",
    "6" : "Número de contato..."

}

def encontrar_resposta(pergunta):
        for palavra_chave, resposta in faq.items():
            if palavra_chave in pergunta:
                return resposta


while True:
    pergunta = input("Digite sua pergunta: ")
    resposta = encontrar_resposta(pergunta)
    print(resposta)
    confirm = input("Deseja fazer mais alguma pergunta? S/N: ")
    confirm = confirm.upper()
    if confirm == "N":
        break
