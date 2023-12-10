from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def main(request):
    return HttpResponse('<h1>Главная страница</h1>')


def product(request, pk):
    return HttpResponse(f'<h1>Главная страница</h1> {pk}')


def news(request):
    return HttpResponseRedirect('shop/3/product')


def card(request, pk):
    name = request.GET.get('prod', 'Noname')
    color = request.GET.get('color')
    size = request.GET.get('size')
    price = request.GET.get('price')
    return HttpResponse(f'<h1>Ваша корзина</h1> {pk}'
                        f'<p>Товар: {name}</p>'
                        f'<p>Цена: {price}</p>'
                        f'<p>Размер: {size}</p>'
                        f'<p>Цвет: {color}</p>')


def order(request, pk):
    return HttpResponse(f'<h1>Ваши заказы</h1> {pk}')


def faq(request, pk):
    return HttpResponse('<h1>Запросы</h1>')
