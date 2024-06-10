n
# Dicionário FAQ com palavras-chave e respostas.
faq_respostas = {
    "1" : "O horário de atendimento é das 9:00 até às 17:00 horas!",
    "2" : "O local de atendimento é na parte leste da empresa ao lado da biblioteca!",
    "3" : "A empresa atualmente reside na Rua Leopoldina Assunção, 1257, Centro, Fortaleza!",
    "4" : "A empresa EnterPrizes é especializada no atendimento e no conforto dos clientes! Nossa empresa dará o melhor para tornar seu ambiente o mais agradável possível para seus clientes!",
    "5" : "No momento, a EnterPrizes atende apenas nas regiões de Fortaleza, Maracanaú, Sobral e Itapipoca!",
    "6" : "Claro! Caso deseje um atendimento humano, use o número +55 (85) 9 9732-2742"

}

#Dicionário Faq das opções do usuário.
faq_perguntas = {
    "1" : "Qual o horário de atendimento?",
    "2" : "Quais os locais em que a empresa trabalha?",
    "3" : "Qual o endereço da empresa EnterPrizes?",
    "4" : "Quais os serviços da empresa?",
    "5" : "Quais são as regiões que a empresa atende?",
    "6" : "Qual número posso usar para entrar em contato?"

}

def encontrar_resposta(pergunta):
        for palavra_chave, resposta in faq_respostas.items():
            if palavra_chave in pergunta:
                return resposta
            else:
                return "Desculpe, não entendi qual sua dúvida."


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
