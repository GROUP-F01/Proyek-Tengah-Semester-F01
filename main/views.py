import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from main.models import Buku
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart_checkout.views import init_cart, add_to_cart
from django.views.decorators.csrf import csrf_exempt
# Creat
def show_main(request):
    buku = Buku.objects.all()

    init_cart(request)

    if request.method == "POST":
        book_id = request.POST.get("book_id")
        add_to_cart(request, book_id)

    amount_added = request.session.get('amount_added', 0)

    context = {
        'user': request.user,
        'name': request.user.username,
        'kumpulanbuku': buku,
        'amount_added': amount_added,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_json(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_buku(request):
    buku = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', buku),content_type="application/json")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                response = HttpResponseRedirect(reverse("inventory_management:literaloka_admin")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    return response