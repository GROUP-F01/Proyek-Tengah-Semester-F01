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
    buku = Buku.objects.all()
    context = {
        'kumpulanbuku': buku,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "admin-page.html", context)

def add_buku(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('inventory_management:literaloka_admin'))

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_xml(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
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
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_product_json(request):
    kumpulan_buku = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', kumpulan_buku))

@csrf_exempt
def add_buku_ajax(request):
    if request.method == 'POST':
        isbn = request.POST.get("isbn")
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        publisher = request.POST.get("publisher")
        publication_date = request.POST.get("publication_date")
        page_count = request.POST.get("page_count")
        category = request.POST.get("category")
        image_url = request.POST.get("image_url")
        lang = request.POST.get("lang")
        price = request.POST.get("price")
        user = request.user

        buku_baru = Buku(isbn=isbn, title=title, author=author, description=description, publisher=publisher, publication_date=publication_date, page_count=page_count, category=category, image_url=image_url, lang=lang, price=price, user=user)
        buku_baru.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# isbn = models.CharField(null=True, blank=True, max_length=255)
#     title = models.CharField(null=True, blank=True, max_length=255)
#     description = models.TextField(null=True, blank=True)
#     author = models.CharField(null=True, blank=True, max_length=255)
#     publisher = models.CharField(null=True, blank=True, max_length=255)
#     publication_date = models.CharField(null=True, blank=True, max_length=255)
#     page_count = models.IntegerField(null=True, blank=True)
#     category = models.CharField(null=True, blank=True, max_length=255)
#     image_url = models.URLField(null=True, blank=True)
#     lang = models.CharField(null=True, blank=True, max_length=255)
#     price = models.IntegerField(null=True, blank=True)