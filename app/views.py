from django.shortcuts import render, redirect
from .models import Pokedex, Rankings, Leagues


def home(request):
    pokemons = Pokedex.objects.all()
    return render(request, 'home.html', {"pokemons": pokemons})


def results(request):
    pokemons = Pokedex.objects.all()
    pokedex = Pokedex.objects.values_list('name', flat=True)
    if request.method == 'POST':
        poke_name = request.POST['poke_name']
        query_results = Rankings.objects.order_by('position').filter(name__contains=poke_name)
        return render(request, 'results.html', {'poke_name': poke_name, 'results': query_results, "pokemons": pokemons, 'pokedex': pokedex})
    else:
        return redirect('home')


# to do

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
