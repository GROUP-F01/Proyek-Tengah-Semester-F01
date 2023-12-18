import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from main.models import Buku
from jualbuku.models import BukuUser
from django.core import serializers
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from functools import wraps
from django.contrib.auth.models import User
from main.models import Buku


from django.views.decorators.csrf import csrf_exempt

def user_not_superuser(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrap

@user_not_superuser
def show_buku(request):
    if(isinstance(request.user, AnonymousUser)) :
        return redirect('main:login')
    
    buku = BukuUser.objects.filter(user=request.user)
    context = {
        'list_buku': buku
    }
    return render(request, "penjualan.html", context)

@user_not_superuser
def create_buku(request):
    if(isinstance(request.user, AnonymousUser)) :
        return redirect('main:login')
    
    if request.method == "POST":
        data = json.loads(request.POST['data'])
        user = request.user
        buku = Buku.objects.create(**data)
        buku_user = BukuUser.objects.create(user=user, buku=buku)
        return JsonResponse(status=201, data={'success': 'true', 'message': "Success create buku"})

    return render(request, "create_buku.html")

def show_xml(request):
    data = BukuUser.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BukuUser.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#Flutter
def all_buku_flutter(request):
    buku = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", buku), content_type="application/json")

def show_buku_flutter(request):
    data = BukuUser.objects.filter(user = request.user)
    books = []
    for bukuUser in data:
        books.append(bukuUser.buku)
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")

@csrf_exempt
def create_buku_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        buku = Buku(
            isbn = data["isbn"],
            title = data["title"],
            description = data["description"],
            author = data["author"],
            publisher = data["publisher"],
            publication_date = data["publication_date"],
            page_count = int(data["page_count"]),
            category = data["category"],
            image_url = data["image_url"],
            lang = data["lang"],
            price = int(data["price"]),
        )
        buku.save()

        bukuUser = BukuUser(
            buku = buku,
            user = request.user,
        )
        bukuUser.save()

        return JsonResponse({
            "status": True,
            "message": 'Buku berhasil dibuat',
        }, status=200)

    return JsonResponse({
        "status": False,
        "message": 'Buku gagal dibuat',
    }, status=400) 

@csrf_exempt
def update_buku_flutter(request):
    if request.method == 'POST':
        data = data = json.loads(request.body)
        print(data["page_count"])
        buku = Buku.objects.get(pk = int(data["pk"]))
        if (BukuUser.objects.get(buku = buku, user = request.user)):
            buku.isbn = data["isbn"]
            buku.title = data["title"]
            buku.description = data["description"]
            buku.author = data["author"]
            buku.publisher = data["publisher"]
            buku.publication_date = data["publication_date"]
            buku.page_count = int(data["page_count"])
            buku.category = data["category"]
            buku.image_url = data["image_url"]
            buku.lang = data["lang"]
            buku.price = int(data["price"])
            buku.save()
            return JsonResponse({
                "status": True,
                "message": 'Buku berhasil diupdate',
            }, status=200)

    return JsonResponse({
        "status": False,
        "message": 'Buku gagal diupdate',
    }, status=400)


@csrf_exempt
def delete_buku_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        buku = Buku.objects.get(pk = data["pk"])
        if (BukuUser.objects.get(buku = buku, user = request.user)):
            buku.delete()
            return JsonResponse({
                "status": True,
                "message": 'Buku berhasil dihapus',
            }, status=200)

    return JsonResponse({
        "status": False,
        "message": 'Buku gagal dihapus',
    }, status=400)
