from django.shortcuts import render
from django.views.generic import View
from .models import *

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)