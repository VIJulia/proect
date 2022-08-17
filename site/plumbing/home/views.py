from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, get_object_or_404
from .models import *


menu=[{'title':"О нас", 'url_name':'about'},
    {'title':"Отзывы", 'url_name':'reviews'},
    {'title':"Контакты", 'url_name':'contact'},
]

def index (request):
    post=Mounting.objects.all() #выбрать все записи из базы данных
    return render(request, 'home/index.html', {'post':post, 'menu':menu,'title': "Монтаж систем отопления и водоснабжения"}) #путь к шаблону


def about (request):
    return render(request, 'home/about.html',{'menu':menu,'title': "О нас"})

def reviews (request):
    return render(request, 'home/reviews.html',{'menu':menu,'title': "Отзывы"})

def contact (request):
    return render(request, 'home/contact.html',{'menu':menu,'title': "Контакты"})

def services (request, ser):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h2>НАШИ УСЛУГИ<h2><p>{ser}<p/>')

def pageNotFound (request, exception):
    return HttpResponseNotFound('<h2> Страница не найдена </h2>') # обработка исключений

def show_services (request, services_id):
    services=get_object_or_404(Mounting, pk=services_id)

    context= {
        'services':services,
        'menu':menu,
        'title':services.title,
    }
    return render(request, 'home/services.html', context=context)