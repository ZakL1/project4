from django.shortcuts import render
from django.contrib import messages
from .models import About
from django.views import generic
from django.http import HttpResponse


# Create your views here.
def about(request):
    return render(request, 'about.html')