from typing import Dict

from django.shortcuts import render
from django.http import *

# def index(request):
#     return HttpResponse("<h1>Olá mundo, Django!</h1>")

def index(request):
    # Constrói um dicionário para passar ao template seu contexto.
    # Note que a chave 'msgnegrito' representa o {{ msgnegrito }} no template!
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}

    # Retorna uma resposta renderizada para enviar ao cliente.
    # Fazemos uso da função de atalho para facilitar tudo.
    # Note que o primeiro parâmetro é o template que desejamos usar.

    return render(request, 'Django/index.html', dicionario_contexto)

 #   return render(request, 'django/more.html', dicionario_contexto2)