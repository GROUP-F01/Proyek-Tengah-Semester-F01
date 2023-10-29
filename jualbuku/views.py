import json
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from main.models import Buku
from jualbuku.models import BukuUser
from django.core import serializers
from django.contrib.auth.models import AnonymousUser

def show_buku(request):
    if(isinstance(request.user, AnonymousUser)) :
        return redirect('main:login')
    
    buku = BukuUser.objects.filter(user=request.user)
    context = {
        'list_buku': buku
    }
    return render(request, "penjualan.html", context)


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