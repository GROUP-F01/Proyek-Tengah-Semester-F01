from django.shortcuts import render
from django.http import HttpResponseRedirect
from jualbuku.forms import InputBuku
from django.urls import reverse
from main.models import Buku
from jualbuku.models import BukuUser

def show_buku(request):
    buku = BukuUser.objects.filter(user=request.user)
    context = {
        'list_buku': buku
    }
    return render(request, "penjualan.html", context)


def create_buku(request):
    form = InputBuku(request.POST or None)

    if form.is_valid() and request.method == "POST":
        buku = form.save(commit=False)
        buku.save()
        print("Halo")
        print(buku.id)
        buku_user = BukuUser(buku = buku, user = request.user)
        buku_user = buku_user.save()
        return HttpResponseRedirect(reverse('jualbuku:jual_buku'))

    context = {'form': form}
    return render(request, "create_buku.html", context)
# Create your views here.
