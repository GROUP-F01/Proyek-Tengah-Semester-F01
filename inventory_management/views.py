import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from main.forms import ProductForm
from django.urls import reverse
from main.models import Buku
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def admin_page(request):
    if request.user.is_staff == False:
        return render(request, 'login.html')
    buku = Buku.objects.all()
    context = {
        'name': request.user.username,
        'kumpulanbuku': buku,
    }

    return render(request, "admin-page.html", context)

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

@csrf_exempt
def login_admin(request):
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
            else:
                return render(request, '')
    context = {}
    return render(request, 'login_admin.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    return response

def get_product_json(request):
    kumpulan_buku = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', kumpulan_buku))

def delete_buku(request, id):
    buku = Buku.objects.get(pk = id)
    buku.delete()
    return HttpResponseRedirect(reverse('inventory_management:literaloka_admin'))

def error_login(request):
    return HttpResponseRedirect(reverse('inventory_management:literaloka_admin'))

@csrf_exempt
def add_buku_ajax(request):
    if request.method == 'POST':
        isbn = request.POST.get("isbn")
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        publisher = request.POST.get("publisher")
        publication_date = request.POST.get("publication-date")
        page_count = request.POST.get("page-count")
        category = request.POST.get("category")
        image_url = request.POST.get("url")
        lang = request.POST.get("lang")
        price = request.POST.get("price")

        buku_baru = Buku(isbn=isbn, title=title, author=author, description=description, publisher=publisher, publication_date=publication_date, page_count=page_count, category=category, image_url=image_url, lang=lang, price=price)
        buku_baru.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

