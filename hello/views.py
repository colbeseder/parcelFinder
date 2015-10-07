from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from .models import Greeting

from fetch import Fetch

# Create your views here.
def index(request):
    f = Fetch(1)
    c = Context({
        "mine"        : f.mine(False),
        "theirs"      : f.theirs(False),
        "mine_safe"   : f.mine(True),
        "theirs_safe" : f.theirs(True)
    })
    return render(request, 'index.html', c)

def result(request):
    c = Context({
        "mine"        : f.mine(False),
        "theirs"      : f.theirs(False),
        "mine_safe"   : f.mine(True),
        "theirs_safe" : f.theirs(True)
    })
    return render(request, 'result.html', c)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

