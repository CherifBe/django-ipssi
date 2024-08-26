from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product, ProductItem
# Create your views here.
def index(request):
    return HttpResponse("<h1>Bonjour à tous !</h1>")

def getProduct(request):
    product = Product.objects.all()
    product_str = ""

    for p in product:
        product_str += p.name + ", "

    return HttpResponse("Liste des produits : " + product_str)