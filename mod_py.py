n
# Dicionário FAQ com palavras-chave e respostas.
# Na esquerda trmos palavras chaves e na direita temos as respostas relacionadas a cada palavra chave.
# Os dois valores estão ligados por conta do ":" e são atribuídos a variáveis mais pra frente.
faq_respostas = {
    "1" : "O horário de atendimento é das 9:00 até às 17:00 horas!",
    "2" : "O local de atendimento é na parte leste da empresa ao lado da biblioteca!",
    "3" : "A empresa atualmente reside na Rua Leopoldina Assunção, 1257, Centro, Fortaleza!",
    "4" : "A empresa EnterPrizes é especializada no atendimento e no conforto dos clientes! Nossa empresa dará o melhor para tornar seu ambiente o mais agradável possível para seus clientes!",
    "5" : "No momento, a EnterPrizes atende apenas nas regiões de Fortaleza, Maracanaú, Sobral e Itapipoca!",
    "6" : "Claro! Caso deseje um atendimento humano, use o número +55 (85) 9 9732-2742"

}

#Dicionário Faq das opções do usuário.
#Na esquerda trmos palavras chaves e na direita temos os valores relacionadas a cada palavra chave.
#Os dois valores estão ligados por conta do ":" e são atribuídos a variáveis mais pra frente.

faq_perguntas = {
    "1" : "Qual o horário de atendimento?",
    "2" : "Quais os locais em que a empresa trabalha?",
    "3" : "Qual o endereço da empresa EnterPrizes?",
    "4" : "Quais os serviços da empresa?",
    "5" : "Quais são as regiões que a empresa atende?",
    "6" : "Qual número posso usar para entrar em contato?"

}

# Função principal que vai encontrar a resposta.
def encontrar_resposta(pergunta):
        #Para cada palavra_chave e resposta nos itens da faq_respostas:
        for palavra_chave, resposta in faq_respostas.items():
            #Se houver uma palavra_chave dentro da pergunta:
            if palavra_chave in pergunta:
                #Retorna o valor correspondente da resposta no faq_RESPOSTAS.
                #Exemplo: Digitei o número "1". Ele vai reconhecer o "1" e responder o que vem depois do ":" na linha do "1" no dicionário faq_RESPOSTAS.
                return resposta
            #Caso nao haja nenhuma palavra_chave dentro da pergunta:
            else:
                #Retorna um valor de string padrão com a mensagem a seguir:
                return "Desculpe, não entendi qual sua dúvida."

#Executa indefinidamente dentro do programa, até see interrompido
while True:
    # Mensagem de boas-vindas:
    print("Digite o número correspondente a sua dúvida!")

    # Serve apenas para printar as opções de perguntas e seus respectivos números.
    # Para cada palavra_chave, resposta nos itens da faq_PERGUNTAS:
    for palavra_chave, resposta in faq_perguntas.items():
        #Exibe todos os valores do dicionário de perguntas:
        print(palavra_chave, resposta)
        
    # Fazendo a pergunta ao usuário e atribuindo a informação dele a uma variável "pergunta", utilizada na função encontrar_resposta.
    # Aqui é o início de todo o código.
    pergunta = input("Digite sua pergunta: ")

    # Aqui eu chamo a função principal, que é responsável por dar um valor a minha variável resposta.
    # Também atribuo o valor dela a uma outra variável resposta.
    resposta = encontrar_resposta(pergunta)

    # Aqui faco aparecer a resposta.
    print(resposta)

    # Função extra para saber se a pessoa deseja fazer outra pergunta.
    confirm = input("Deseja fazer mais alguma pergunta? S/N: ")

    # Tornando a resposta em letras maiúsculas para facilitar o entendimento da máquina.
    confirm = confirm.upper()

    # Se a resposta for "N" ele dá um "break" no looping e o código acaba.
    if confirm == "N":
        break
