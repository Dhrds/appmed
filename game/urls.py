from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.index, name='index'),
    path('', views.jogo_adivinhacao, name='jogo_adivinhacao'),
    path("diagnostico/", views.diagnostico, name='iniciar_diagnostico'),
    path("processar_resposta/", views.processar_resposta,
         name='processar_resposta'),
]