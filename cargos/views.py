from django.shortcuts import render
from cargos.forms import CargoForm, TransferForm, RentsForm, RootTrForm
from cargos.models import Auto, Roots


def add_cargo(request):
    form = CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CargoForm()

    context = {
        'form': form
    }
    return render(request, 'cargo/addcargo.html', context)


def add_transfer(request):
    form = TransferForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TransferForm()

    content = {
        'form': form
    }
    return render(request, 'cargo/addtransfer.html', content)


def rent(request):
    form = RentsForm(request.POST or None)
    cars = Auto.objects.all()
    if form.is_valid():
        form.save()
        form = RentsForm()

    cont = {
        'form': form,
        'cars': cars
    }
    return render(request, 'cargo/service.html', cont)


def rootTr(request):
    form = RootTrForm(request.POST or None)
    roots = Roots.objects.all()
    if form.is_valid():
        form.save()
        form = RootTrForm

    content = {
        'form': form,
        'roots': roots
    }
    return render(request, 'cargo/root-transfer.html', content)
