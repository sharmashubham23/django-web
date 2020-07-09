from django.shortcuts import render, HttpResponse
from shop.models import Product

# Create your views here.


def shophome(request):
    products = Product.objects.all()
    print("=============================================================")
    print(products)
    print("=============================================================")
    params = {'product': products}
    return render(request, 'shop/shophome.html', params)


def productview(request):
    products = Product.objects.all()
    # print("=============================================================")
    # print(products)
    # print("=============================================================")
    params = {'product': products}
    return render(request, 'shop/productview.html', params)
