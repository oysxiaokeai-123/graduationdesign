from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponseRedirect


def start(request):
    return render(request, 'start.html')

