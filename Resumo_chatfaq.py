#Biblioteca crucial para o funcionamento do código - Favor baixar no terminal com "pip install fuzzywuzzy"
from fuzzywuzzy import fuzz

#Funções do python
import unicodedata
import string

# Dicionário FAQ com palavras-chave e respostas
faq = {
    # Horário de atendimento
    ("horario de atendimento",
     "horario atendimento",
     "horas do atendimento",
     "horas atendimento"): "O horário de atendimento de todas as unidades é de 9:00 ás 19:00 horas.",

    # Sedes no Brasil
    ("sedes no brasil",
     "sedes do brasil",
     "sedes da empresa",
     "sedes dessa empresa"): "A Etical Enterprises tem 5 sedes espalhadas pelo Brasil. Uma no Rio de Janeiro, duas em São Paulo e duas no Ceará.",

    # Rio de Janeiro - Localização
    ("sede no rio de janeiro",
     "sede do rio de janeiro",
     "sede rio de janeiro",
     "rio de janeiro sede"): "A sede do Rio de Janeiro fica na rua De Leonardo Pravo, N* 1500, Nerlin, São Gonçalo, e funciona das 9:00 ás 19:00 horas.",

    # Rio de Janeiro - São Gonçalo - Horários
    ("horario de sede no rio de janeiro",
     "horario da sede no rio de janeiro",
     "horario de atendimento rio de janeiro",
     "até que horas no rio de janeiro",
     "horario de sede em sao gonçalo",
     "horario da sede em sao gonçalo",
     "horario de atendimento sao gonçalo",
     "até que horas em sao gonçalo"): "O horário de funcionamento da sede na cidade de São Gonçalo é das 9:00 até as 19:00 horas.",

    # Rio de Janeiro - São Gonçalo - Local
    ("rua da sede no rio de janeiro",
     "a sede do rio de janeiro",
     "local da da sede no rio de janeiro",
     "localidade da sede no rio de janeiro",
     "endereço da sede no rio de janeiro",
     "rua da sede em sao gonçalo",
     "a sede de sao gonçalo",
     "a sede em sao gonçalo",
     "local da da sede em sao gonçalo",
     "localidade da sede em sao gonçalo",
     "endereço da sede em sao gonçalo"): "A sede do Rio de Janeiro fica na rua De Leonardo Pravo, N* 1500, Nerlin, São Gonçalo.",

    # São Paulo - Localização geral
    ("sedes em sao paulo",
     "sedes de sao paulo",
     "sedes sao paulo",
     "sao paulo sedes"): "As sedes em São Paulo ficam ambas na cidade de São Paulo, uma no bairro Liberdade e outra no Centro,.",

    # São Paulo - Centro - Horários
    ("horario de sede no centro",
     "horario da sede no centro",
     "horário de atendimento centro",
     "até que horas no centro"): "O horário de funcionamento da sede na cidade de São Paulo é das 9:00 até as 19:00 horas.",

    # São Paulo - Centro - Local
    ("rua da sede no centro",
     "a sede no centro",
     "local da da sede no centro",
     "localidade da sede no centro",
     "endereço da sede no centro"): "A sede no Centro de São Paulo fica na Rua Moçarique Medeiros, N* 1390, Centro, São Paulo.",

    # São Paulo - Guarulhos - Horários
    ("horario de sede em guarulhos",
     "horario da sede em guarulhos",
     "horário de atendimento guarulhos",
     "até que horas em guarulhos"): "O horário de funcionamento da sede em Guarulhos é das 9:00 até as 19:00 horas.",

    # São Paulo - Guarulhos - Local
    ("rua da sede em guarulhos",
     "a sede em guarulhos",
     "local da da sede em guarulhos",
     "localidade da sede em guarulhos",
     "endereço da sede em guarulhos"): "A sede em Guarulhos fica na Rua Marvelick, N* 349, Liberdade, São Paulo.",

    # Ceará - Localização geral
    ("sedes no ceara",
     "sedes do ceara",
     "sede do ceara",
     "ceara sedes",
     "sedes ceara"): "As sedes do Ceará ficam nas cidades de Fortaleza, Aldeota, e Maracanaú, Pajuçara.",

    # Ceará - Fortaleza - Horários
    ("horario da sede em fortaleza",
     "horario da sede em fortaleza",
     "horário de atendimento sede fortaleza",
     "até que horas em fortaleza"): "O horário de funcionamento da sede em fortaleza é das 9:00 até as 19:00 horas.",

    # Ceará - Fortaleza - Local
    ("rua da sede em fortaleza",
     "a sede em fortaleza",
     "local da da sede em fortaleza",
     "localidade da sede em fortaleza",
     "endereço da sede em fortaleza",
     "rua da sede de fortaleza",
     "local da da sede de fortaleza",
     "localidade da sede de fortaleza",
     "endereço da sede de fortaleza"): "A sede na cidade de Fortaleza fica na Rua Leopodina da Assunção, N* 472, Aldeota, Fortaleza.",

    # Ceará - Maracanaú - Horários
    ("horario de sede em maracanau",
     "horario da sede em maracanau",
     "horário de atendimento sede em maracanau",
     "até que horas em maracanau"): "O horário de funcionamento da sede em Maracanaú é das 9:00 até as 19:00 horas",

    # Ceará - Maracanaú - Local
    ("rua da sede no maracanau",
     "a sede em maracanau",
     "rua da sede no maracanau",
     "local da sede no maracanau",
     "endereço da sede no maracanau"
     "rua da sede em maracanau",
     "rua da sede em maracanau",
     "local da sede em maracanau",
     "endereço da sede em maracanau"): "A sede na cidade de Maracanaú fica na rua Padre Figueiredo, N* 668, Pajuçara, Fortaleza.",
}

# Função para retirar os acentos e substituir por caracteres sem acento
def retirar_acento(texto):
    return "".join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

#Função principal que encontra a melhor resposta para a pergunta feita baseada na similaridade de texto.
def encontrar_resposta(pergunta):
    #Variável pergunta vai receber o valor da pergunta sem acento e sem pontuações.
    #Função retirar acento é chamado aqui.
    #Dentro dela a pergunta também se torna totalmente em minuscula. "pergunta.lower()."
    #Translate atue como um "tradutor" que traduz o texto dela que, basicamente, retiram as strings das pontuações da pergunta.
    #Isso tudo é para que a pergunta se torna mais fácil de análisar e não precise ser tão especifica.
    pergunta = retirar_acento(pergunta.lower().translate(str.maketrans("", "", string.punctuation)))

    #Cria uma variável que armazena a pergunta em forma de tokens, ou seja, separa a pergunta em
    #palavras diferentes, mas que pertecem ao mesmo valor tokens_pergunta.
    #Exemplo: "Água é bom", se torna, "/Água/", "/é/", "/bom/".
    tokens_pergunta = set(pergunta.split())

    #Variável pra armazenar a melhor resposta.
    melhor_resposta = None

    #Score que a máquina vai determinar como melhor ou não.
    melhor_score = 0

    #Para cada palavra_chave e resposta em faq.items():
    #Faq é a biblioteca que armazena o valores das palavras chaves e das repostas pra cada um.
    #Aqui ele vai rodar cada palavra chave dos itens do faq até que o melhor valor seja obtido, ou não.
    for palavra_chave, resposta in faq.items():

        #Aqui eu estou tornando as palavras chaves do meu faq, TODAS ELAS, em tokens, que já expliquei antes.
        #Mesmo separados em tokens, a máquina ainda identifica eles como uma frase só aqui.
        tokens_chave = set(" ".join(palavra_chave).split())

        #Aqui eu dou um valor para o score que vai ser a interseção entre os TOKENS da pergunta
        #e os TOKENS da resposta, ou seja, ele compara a pergunta feita com a palavras chaves, só
        #tudo em formato de token pra que ele consiga análisar palavra por palavra, ao invés de
        #análisar a frase toda da palavra chave.
        score = len(tokens_pergunta.intersection(tokens_chave))

        #Para cada palavra em palavra_chave:
        #Aqui crio uma variável temporária "palavra" que armazena cada palavra dentro da palavra_chave
        for palavra in palavra_chave:

            #Aqui crio uma variável para armazenar a similiridade, novamente, entre cada palavra na
            #palavra chave, porém usando uma funçao da biblioteca Fuzzy.
            #Isso serve pra, basicamente, verificar o quão similar minha pergunta é com as palavras
            #chaves que tenho no meu faq, pois o processo de antes iria responder alguma resposta
            #do meu faq, mesmo que a pessoas digitasse "daolfjlsahfoj", ele ainda iria responder algo.
            #Aqui ele vai analisar a similaridade e, caso não seja tão similar, ele vai me dar a possibilidade
            #de retornar a resposta "Desculpe, não entendi sua pergunta."
            similaridade = fuzz.partial_ratio(palavra, pergunta)

            #Aqui estou definindo o quão similar ele precisar ser e, caso não seja tão similar
            #quanto eu quiser, ele vai retornar lá embaixo um valor fixo pra resposta.
            if similaridade > 90:

                #Aqui eu faço a variável score aumentar em 1, o que me permite iniciar o próximo
                #passo do código logo abaixo desse.
                score += 1

        #Pre final do codigo que só executa quando o codigo td já fez seu trabalho
        #Se score for maior que melhor resposta, o que é obrigatorio acontecer no final do codigo
        if score > melhor_score:

            #Torno as variáveis de antes sem valor nenhum dentro nos resultados que obtive.
            melhor_score = score
            melhor_resposta = resposta

    # Aqui, enfim, eu uso aqueles valores de antes e definir as principais respostas.
    #Se o melhor_score for maior do que 0, ou seja, ele sempre vai ser obrigatoriamente maior do
    #que 0 quando o código executar tudo, ou seja, isso só executa quando tudo já foi executado nessa função

    if melhor_score > 0:

        #Retornando a melhor_resposta para a variável resposta definida no início da função.
        #Lembrando que melhor_resposta é igual a variavel reposta, que é a que armazena a resposta desde o inicio.
        return melhor_resposta
    else:

        #Aqui retorno o valor para a reposta caso, como disse antes, o score não seja maior do que 0.
        #Isso vai acontecer quando a similaridade, que defini como 90, não for suficiente, ou seja
        #O if similaridade não vai executar o valor que faz o score += 1 acontecer e o score é apenas 0.
        return "Desculpe, não entendi sua pergunta."

#Função já explicada em aula que sempre executar até ser falso.
while True:

    #Fazendo a pergunta para o usuário.
    pergunta = input("Digite sua pergunta: ")

    #Atribuindo o valor obtido da minha função para a variável resposta.
    resposta = encontrar_resposta(pergunta)

    #Resposta do bot
    print(resposta)

    #Função pra terminar o processo de perguntar e acabar com o loop.
    confirm = input("Deseja fazer mais alguma pergunta? S/N: ")
    confirm = confirm.upper()
    if confirm == "N":
        break
