from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Paciente, Doenca
import openai
import os

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


def index(request):
    return render(request, 'index.html')


def diagnostico(request):
    paciente = get_object_or_404(Paciente, id=2)
    doenca = get_object_or_404(Doenca, id=2)
    context = {'paciente': paciente,
               'conversa': ''}
    if request.method == 'POST':
        nome_medico = request.POST.get('nome_medico')
        crm_medico = request.POST.get('crm_medico')
        especialidade = request.POST.get('especialidade')
        pergunta_selecionada = request.POST.get('pergunta')
        respostas = request.POST.get('resposta')

        if pergunta_selecionada == 'pergunta_1':
            context['conversa'] += (respostas)
            context['conversa'] += ('P: Qual é o principal sintoma apresentado pelo paciente?') # noqa
            context['conversa'] += (f'\n R: {doenca.sintomas}')
        elif pergunta_selecionada == 'pergunta_2':
            context['conversa'] += (respostas)
            context['conversa'] += ('P: O paciente possui algum histórico médico relevante? (ex: doenças crônicas, alergias)') # noqa
            context['conversa'] += (f'\n R: {doenca.descricao}')
        elif pergunta_selecionada == 'pergunta_3':
            context['conversa'] += (respostas)
            context['conversa'] += ('P: Existe algum fator desencadeante conhecido para os sintomas apresentados?') # noqa
            context['conversa'] += (f'\n R: {doenca.descricao}')
        context['nome_medico'] = nome_medico
        context['crm_medico'] = crm_medico
        context['especialidade'] = especialidade
        print(context['conversa'])
    return render(request, 'diagnostico.html', context)


def processar_resposta(request):
    return HttpResponse("Método HTTP não suportado")


def jogo_adivinhacao(request):
    if request.method == 'POST':
        sintoma = request.POST.get('sintoma', '')
        mensagem = request.POST.get('mensagem', '')
        response = enviar(sintoma, [{'role': 'system', 'content': mensagem}])
        return render(request, 'jogo_adivinhacao.html', {
            'resposta': response["content"]})
    return render(request, 'jogo_adivinhacao.html', {'resposta': None})
