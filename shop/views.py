from django.shortcuts import render, HttpResponse
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def shophome(request):
    products = Product.objects.all()
    params = {'product': products}
    return render(request, 'shop/shophome.html', params)


def productview(request, myid):

    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product': product[0]})


def logincheckout(request):
    messages.warning(request, "Please LogIn or SingUp before checkout ")
    return render(request, 'shop/shophome.html')


@login_required(login_url='/shop/logincheckout/')
def checkout(request):
    return render(request, 'shop/checkout.html')


def cart(request):
    return render(request, 'shop/cart.html')
