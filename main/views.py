from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'namapage': 'Landing page utama',
    }

    return render(request, "main.html", context)

