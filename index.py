perguntaUm = "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?"
perguntaDois = "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?"
perguntaTres = "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?"
perguntaQuatro = "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?"
perguntaCinco = "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?"
perguntaSeis = "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?"
perguntaSete = "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE."

respostaUm = "O nome da protagonista é Joan Tait. "
respostaDois = "A inteligência artificial dirige a vida de Joan."
respostaTres = "Streamberry."
respostaQuatro = "Ao procurar algo para assistir com o noivo ela se depara com a série."
respostaCinco = "Joan ficou em choque, como resposta ela decide tomar atitudes que pudessem indignar outra pessoa com mais voz e poder que ela."
respostaSeis = " Os episódio trata sobre captação de dados, consentir permissões de uso sem ler, inteligência artificial, deep fake, privacidade."
respostaSete = "Não termina de forma típica por que acaba tendo um final feliz."

while True:
    pergunta = input("Digite sua pergunta sobre Black Mirror: ")
    if pergunta == perguntaUm:
        print(respostaUm)
    elif pergunta == perguntaDois:
        print(respostaDois)
    elif pergunta == perguntaTres:
        print(respostaTres)
    elif pergunta == perguntaQuatro:
        print(respostaQuatro)
    elif pergunta == perguntaCinco:
        print(respostaCinco)
    elif pergunta == perguntaSeis:
        print(respostaSeis) 
    elif pergunta == perguntaSete:
        print(respostaSete)
    else:
        print("Pergunta inválida")