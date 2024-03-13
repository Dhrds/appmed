import openai
import os
# flake8: noqa E501
openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )
    lista_mensagens.append(response["choices"][0]["message"])

    return response["choices"][0]["message"]


def jogar_adivinhacao_doenca():
    print("Bem-vindo ao jogo de adivinhação de doenças!")
    print("Pense em uma doença e me dê alguns sintomas.")

    doenca = "IVAS (Resfriado comum)"
    lista_mensagens = [
        {
            "role": "system", "content":
                f"""Estou brincando de adivinhar o que é,
                Quero fazer um jogo com vc,
                vou te falar uma doença e quero que você simule que tenha essa doença,
                você será o paciente respondendo sim ou não sobre os sintomas
                que eu vou te falar,
                quando eu te pedir os exames quero que você simule um exame que
                indique positivo para a doença escolhida,
                caso eu te peço outra coisa peça para eu voltar a falar sobre a doença,
                você não pode falar o nome da doença, se eu conseguir de parabéns,
                
                a doença é  IVAS (Resfriado comum)

                você é uma Paciente de 50 anos de idade apresentou quadro de cefaleia,
                dor de garganta e  espirros há 5 dias, com aparecimento de tosse purulenta ,
                obstrução nasal, rinorreia anterior e  mal-estar  há 2 dias.
                Relata que intensidade dos sintomas aumentaram até o terceiro dia e agora está em um platô,
                nega febre, alterações no apetite, sono, fraqueza e peso, nega dispneia, dor torácica ,
                cianose e chieira 
"""
        },
    ]

    while True:
        sintoma = input(
            "Digite um sintoma da doença ou 'fim' para terminar: ").strip()
        if sintoma.lower() == 'fim':
            break
        else:
            response = enviar(sintoma, lista_mensagens)
            print("AppMed :", response["content"])


if __name__ == "__main__":
    jogar_adivinhacao_doenca()
