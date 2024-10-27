from django.shortcuts import render
from django.http import HttpResponse

from .models import Buyer, Game
from .forms import UserRegister


def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fourth_task/shop.html', context)


def shop_cart(request):
    return render(request, 'fourth_task/shop_cart.html')


def sign_up_by_django(request):
    # users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age'] 
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        else:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)
