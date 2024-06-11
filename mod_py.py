import random
# Dicionário FAQ com palavras-chave e respostas.
# Na esquerda trmos palavras chaves e na direita temos as respostas relacionadas a cada palavra chave.
# Os dois valores estão ligados por conta do ":" e são atribuídos a variáveis mais pra frente.
# Dicionário FAQ com palavras-chave e respostas.
faq_respostas = {
    "1": "O horário de atendimento é das 9:00 até às 17:00 horas!",
    "2": "O local de atendimento é na parte leste da empresa ao lado da biblioteca!",
    "3": "A empresa atualmente reside na Rua Leopoldina Assunção, 1257, Centro, Fortaleza!",
    "4": "A empresa EnterPrizes é especializada no atendimento e no conforto dos clientes! Nossa empresa dará o melhor para tornar seu ambiente o mais agradável possível para seus clientes!",
    "5": "No momento, a EnterPrizes atende apenas nas regiões de Fortaleza, Maracanaú, Sobral e Itapipoca!",
    "6": "Claro! Caso deseje um atendimento humano, use o número +55 (85) 9 9732-2742",
    "7": "Nossa política de devolução permite devoluções dentro de 30 dias da compra, com reembolso completo ou troca por outro serviço.",
    "8": "Atualmente, não oferecemos serviços de design para residências, apenas para espaços comerciais e empresariais.",
    "9": "Aceitamos pagamentos via transferência bancária, cartão de crédito, e boleto.",
    "10": "O prazo de entrega para projetos de design varia entre 2 a 4 semanas, dependendo da complexidade do projeto.",
    "11": "Sim, oferecemos suporte durante 6 meses após a conclusão do projeto para quaisquer ajustes ou dúvidas.",
    "12": "Nossos designers de interiores possuem qualificações e certificações reconhecidas, além de vasta experiência no mercado.",
    "13": "Sim, oferecemos serviços de consultoria para ajudar a definir o melhor design para seu espaço.",
    "14": "Para agendar uma consulta, entre em contato conosco pelo telefone ou através do nosso site.",
    "15": "Sim, oferecemos descontos para projetos de grande escala. Entre em contato para mais detalhes.",
    "16": "Sim, incorporamos práticas de sustentabilidade em nossos projetos, utilizando materiais eco-friendly sempre que possível.",
    "17": "Você pode acompanhar o progresso do seu projeto através de reuniões periódicas e relatórios semanais enviados por e-mail.",
    "18": "Atualmente, trabalhamos apenas nas regiões mencionadas. Para outras áreas, entre em contato para discutirmos a viabilidade.",
    "19": "Nosso processo de criação inclui uma reunião inicial, desenvolvimento do conceito, apresentação do projeto e implementação.",
    "20": "Sim, oferecemos serviços de renovação completa para espaços comerciais e empresariais.",
    "21": "Quer ver algumas de nossas obras anteriores? Visite nosso portfólio online em www.enterprizes-portfolio.com!",
    "22": "Interessado em tendências atuais de design de interiores? Acesse nosso blog em www.enterprizes-blog.com!"
}

faq_perguntas = {
    "1": "Qual o horário de atendimento?",
    "2": "Quais os locais em que a empresa trabalha?",
    "3": "Qual o endereço da empresa EnterPrizes?",
    "4": "Quais os serviços da empresa?",
    "5": "Quais são as regiões que a empresa atende?",
    "6": "Qual número posso usar para entrar em contato?",
    "7": "Qual é a política de devolução da empresa?",
    "8": "Vocês oferecem serviços de design para residências?",
    "9": "Quais métodos de pagamento são aceitos?",
    "10": "Qual é o prazo de entrega para projetos de design?",
    "11": "A empresa oferece suporte após a conclusão do projeto?",
    "12": "Quais são as qualificações dos designers de interiores da empresa?",
    "13": "Vocês oferecem serviços de consultoria?",
    "14": "Como posso agendar uma consulta com um designer de interiores?",
    "15": "Há descontos para projetos de grande escala?",
    "16": "Vocês trabalham com sustentabilidade nos projetos?",
    "17": "Como posso acompanhar o progresso do meu projeto?",
    "18": "A empresa trabalha com clientes fora das áreas mencionadas?",
    "19": "Qual é o processo de criação de um projeto de design de interiores?",
    "20": "Vocês oferecem serviços de renovação completa?",
    "21": "Onde posso ver projetos anteriores?",
    "22": "Como posso ficar atualizado sobre tendências de design?"
}


# Função principal que vai encontrar a resposta.
def encontrar_resposta(pergunta):
    # Para cada palavra_chave e resposta nos itens da faq_respostas:
    for palavra_chave, resposta in faq_respostas.items():
        # Se houver uma palavra_chave dentro da pergunta:
        if palavra_chave == pergunta:
            # Retorna o valor correspondente da resposta no faq_RESPOSTAS.
            # Exemplo: Digitei o número "1". Ele vai reconhecer o "1" e responder o que vem depois do ":" na linha do "1" no dicionário faq_RESPOSTAS.
            return resposta
    # Caso nao haja nenhuma palavra_chave dentro da pergunta, o looping termina e naõ retorna nenhum valor.
    #Sobrando apenas executar o valor padrão abaixo.
    # Retorna um valor de string padrão com a mensagem a seguir:
    return "Desculpe, não entendi qual sua dúvida."

#Apenas uma saudação aleatória a cada novo início de loop.
def saudacao_inicial():
    saudacoes = [
        "Olá! Como posso ajudar hoje?",
        "Bem-vindo! Em que posso assisti-lo?",
        "Oi! Precisa de alguma informação?",
        "Olá! Seja bem-vindo!"
    ]
    #retorna um valor aleatório dentro do dicionario para a variável
    return random.choice(saudacoes)

# Executa indefinidamente dentro do programa, até ser interrompido
while True:
    # Apenas printando espaços vazios no prompt para organização.
    print("")
    # Mensagem de boas-vindas aleatória:
    print(saudacao_inicial())
    print("")
    #Mensagem de comando padrão:
    print("Digite o número correspondente à sua dúvida:")
    print("")

    # Serve apenas para printar as opções de perguntas e seus respectivos números.
    # Para cada palavra_chave, resposta nos itens da faq_PERGUNTAS:
    for palavra_chave, resposta in faq_perguntas.items():
        # Exibe todos os valores do dicionário de perguntas:
        print(f"{palavra_chave}: {resposta}")

    # Fazendo a pergunta ao usuário e atribuindo a informação dele a uma variável "pergunta", utilizada na função encontrar_resposta.
    # Aqui é o início de todo o código.
    print("")
    pergunta = input("Digite sua pergunta: ")

    # Aqui eu chamo a função principal, que é responsável por dar um valor a minha variável resposta.
    # Também atribuo o valor dela a uma outra variável resposta.
    resposta = encontrar_resposta(pergunta)

    # Aqui faco aparecer a resposta.
    print("")
    print(resposta)

    # Função extra para saber se a pessoa deseja fazer outra pergunta.
    print("")
    confirm = input("Deseja fazer mais alguma pergunta? S/N: ")

    # Tornando a resposta em letras maiúsculas para facilitar o entendimento da máquina.
    confirm = confirm.upper()

    # Se a resposta for "N" ele dá um "break" no looping e o código acaba.
    if confirm == "N":
        break
    else:
        #Apenas printando espaços vazios no prompt.
        print("")
        print("")

