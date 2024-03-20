from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context: dict ={
        'title' : 'HOME - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html',context)

def about(request):
    context: dict ={
        'title' : 'О нас',
        'content': 'О нас',
        'text_on_page': 'текст описания нашего магазина'
    }
    return render(request, 'main/about.html',context)

