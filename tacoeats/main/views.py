from django.shortcuts import render
from django.http import HttpResponse
from .models import Shops
import random
from django import template

def index(request):
    shopList = random.choice(Shops.objects.all())

    return render(
        request,
        'main/index.html',
        context = {'shop_list': shopList})
