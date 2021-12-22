from django.shortcuts import render
from django.http import HttpResponse
from .models import Items

def index(request):
    itemList = Items.objects.all()

    return render(
        request,
        'main/index.html',
        context = {'item_list': itemList})
