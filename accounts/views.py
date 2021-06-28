from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from cargos.models import Сonveyor, Cargo, Transfer, Rents


def index_view(request):
    transport_list = Сonveyor.objects.count()
    cargo = Cargo.objects.count()
    cargo_transfers = Transfer.objects.count()
    services = Rents.objects.count()
    content = {
        'transport_list': transport_list,
        'cargo': cargo,
        'cargo_transfers': cargo_transfers,
        'services': services
    }
    return render(request, 'home/home.html', content)


def show_cargo_list(request):
    conveyor = Сonveyor.objects.all()
    return render(request, 'home/cargo-list.html', {'conveyor': conveyor})


def user_page_view(request):
    my_cargos = Cargo.objects.filter(cargo_owner=request.user)
    my_transfers = Transfer.objects.filter(user=request.user)
    rent = Rents.objects.filter(username=request.user)
    data = {
        'my_cargos': my_cargos,
        'my_transfers': my_transfers,
        'rent': rent
    }
    return render(request, 'user/user-page.html', data)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:user')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:user')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
