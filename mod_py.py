# Dicionário FAQ com palavras-chave e respostas.
faq_respostas = {
    "1" : "O horário de atendimento é...",
    "2" : "O local de atendimento é na...",
    "3" : "O endereço da rua é...",
    "4" : "A empresa é especializada em...",
    "5" : "Serviços de atendimento nas regiões...",
    "6" : "Número de contato..."

}

#Dicionário Faq das opções do usuário.
faq_perguntas = {
    "1" : "Qual o horário de atendimento",
    "2" : "Quais os locais em que a empresa trabalha",
    "3" : "Qual o endereço da empresa em Fortaleza",
    "4" : "Qual os serviços da empresa",
    "5" : "Quais são as regiões que a empresa atende",
    "6" : "Qual número posso usar para entrar em contato"

}

def encontrar_resposta(pergunta):
        for palavra_chave, resposta in faq_respostas.items():
            if palavra_chave in pergunta:
                return resposta


while True:
    print("Digite o número correspondente a sua dúvida!")
    for palavra_chave, resposta in faq_perguntas.items():
        print(palavra_chave, resposta)
    pergunta = input("Digite sua pergunta: ")
    resposta = encontrar_resposta(pergunta)
    print(resposta)
    confirm = input("Deseja fazer mais alguma pergunta? S/N: ")
    confirm = confirm.upper()
    if confirm == "N":
        break
