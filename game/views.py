from django.shortcuts import render
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar(mensagem, lista_mensagens=[], reiniciar=False):
    if reiniciar:
        lista_mensagens = []
    if not lista_mensagens:
        lista_mensagens.append(
            {
                "role": "system", "content":
                """
Estou brincando de adivinhar o que é,
Quero fazer um jogo com vc,
vou te falar uma doença e quero que você simule que tenha essa doença,
você será o paciente respondendo sim ou não sobre os sintomas
que eu vou te falar,
quando eu te pedir os exames quero que você simule um exame que
indique positivo para a doença escolhida,
caso eu te peço outra coisa peça para eu voltar a falar sobre a doença,
você não pode falar o nome da doença, se eu conseguir de parabéns,

a doença é  IVAS (Resfriado comum)

você se chama José é uma Paciente de 50 anos de idade
apresentou quadro de cefaleia,
dor de garganta e  espirros há 5 dias, com aparecimento de tosse purulenta ,
obstrução nasal, rinorreia anterior e  mal-estar  há 2 dias.
Relata que intensidade dos sintomas aumentaram até o terceiro dia e agora está
em um platô, nega febre, alterações no apetite, sono, fraqueza e peso,
nega dispneia, dor torácica ,
cianose e chieira

sua primeira e somente a primeira interação sera
'Olá, meu nome é José e tenho 50 anos. Aguardarei suas perguntas sobre os sintomas.'
                """ # noqa E501
            }
        )
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    print(lista_mensagens)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )
    print(response)
    lista_mensagens.append(response["choices"][0]["message"])

    return lista_mensagens


def jogo_adivinhacao(request):

    if request.method == 'GET':
        response = ''
        response = enviar('', reiniciar=True)
        print(response)
    if request.method == 'POST':
        mensagem_atual = request.POST.get('mensagem', '')
        reiniciar = bool(request.POST.get('reiniciar', False))
        if reiniciar:
            response = ''
        response = enviar(mensagem_atual, reiniciar=reiniciar)
        return render(request, 'chat.html', {
            'resposta': response})
    return render(request, 'chat.html', {'resposta': response})
