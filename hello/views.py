from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from .models import Greeting

from board import *

game_board = Board()


# Create your views here.
def index(request):
    f = Fetch(game_board, 1)
    c = Context({
        "mine"        : f.mine(),
        "theirs"      : f.theirs()
    })
    return render(request, 'index.html', c)

def result(request):
    f = Fetch(game_board, 1)
    
    if request.method == 'POST':
        f.set_mine("'newly set'")
    
    c = Context({
        "mine"        : f.mine(),
        "theirs"      : f.theirs()
    })
    return render(request, 'result.html', c)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

