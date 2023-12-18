from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from main.models import Buku
from resensi.models import Resensi

def get_resensi(request):
    resensi = Resensi.objects.all()
    return HttpResponse(serializers.serialize('json', resensi.all()), content_type="application/json")

@csrf_exempt
def get_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        buku = Buku.objects.filter(pk=data["pk"])
        return HttpResponse(serializers.serialize('json', buku.all()), content_type="application/json")
    
    return HttpResponse(serializers.serialize('json', []), content_type="application/json")

@csrf_exempt
def resensi_buku(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        buku = Buku.objects.get(pk=data["pk"])
        resensi = Resensi.objects.filter(book=buku)
        return HttpResponse(serializers.serialize('json', resensi.all()), content_type="application/json")
    
    return HttpResponse(serializers.serialize('json', []), content_type="application/json")

@csrf_exempt
def create_resensi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        buku = Buku.objects.get(pk=data["pk"])

        Resensi(
            user = request.user,
            book = buku,
            published_by = request.user.username,
            resensi = data["resensi"],
        ).save()
        return JsonResponse({"status": True}, status=200)
    
    return JsonResponse({"status": False}, status=500)

@csrf_exempt
def delete_resensi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        resensi = Resensi.objects.get(pk=data["resensi_id"])
        if resensi.user == request.user:
            resensi.delete()
            return JsonResponse({"status": True}, status=200)
    
    return JsonResponse({"status": False}, status=500)

@csrf_exempt
def edit_resensi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        resensi = Resensi.objects.get(pk=data["resensi_id"])
        if resensi.user == request.user:
            resensi.resensi = data["resensi"]
            resensi.save()
            return JsonResponse({"status": True}, status=200)
    
    return JsonResponse({"status": False}, status=500)
