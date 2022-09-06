from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import RequestContext
from .forms import MainUserCreationForm
from .models import CustomUser, Deck

# Create your views here.


def index(request):
    return render(request, 'game/index.html')


def room(request, room_name):
    if request.method == 'POST':

        print(request.POST)
        deck = Deck.objects.get(pk=request.POST['deck_id'])

        context = {
            'room_name': room_name,
            'deck': deck
        }

        return render(request, 'game/room.html', context)
    else:
        return redirect('index')


def registration(request):
    if request.method == 'POST':
        form = MainUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return render(request, 'game/index.html')

    else:
        form = MainUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'game/register.html', context)
