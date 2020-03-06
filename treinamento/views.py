from django.shortcuts import render

from django.http import HttpResponse
from .models import Pelagem


def index(request):
    latest_question_list = Pelagem.objects.order_by('data_nascimento')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'treinamento.index.html', context)