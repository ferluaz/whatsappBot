import random

R_EATING = "Eu n gosto de comer nd pq sou um robo"


def unknown():
    response = ["",
                "...",
                "Me parece certo",
                "Oque isso significa?",
                "N entendi, poderia escrever novamente?",
                "?????",
                "Doug saiu no momento e provavelmente esqueceu de me desatiavr, sou um bot crado por ele"][
        random.randrange(6)]
    return response