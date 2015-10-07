from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context

from .models import Greeting

from fetch import Fetch


# Create your views here.
def index(request):
    c = Context({
		"mine":"a",
		"theirs":"b"
	})
    return render(request, 'index.html', c)

def result(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'result.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

