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
    for palavra_chave in pergunta:
        if pergunta == "1":
            print("estou funcionando")
        elif pergunta == "2":
            print("pao com banana")
        elif pergunta == "3":
            print("Teste ando")
        elif pergunta == "4":
            print("numero 4")
        elif pergunta == "5":
            print("número 5")
        elif pergunta == "6":
            print("numero 6")


while True:
    pergunta = input("Digite sua pergunta: ")
    resposta = encontrar_resposta(pergunta)
    confirm = input("Deseja fazer mais alguma pergunta? S/N: ")
    confirm = confirm.upper()
    if confirm == "N":
        break
