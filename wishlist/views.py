from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from .models import Wishlist
from .forms import WishlistForm
import json

@require_http_methods(['GET'])
@login_required(login_url='/login')
def show_wishlist(request):
    return render(request, 'wishlist.html')

@require_http_methods(['POST', 'GET'])
@login_required(login_url='/login')
def add_to_wishlist(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return HttpResponseRedirect(reverse('wishlist:show_wishlist'))
        else:
            return render(request, 'forms_wishlist.html', {'form': form})

    form = WishlistForm()
    response = {
        "form": form,
    }
    return render(request, 'forms_wishlist.html', response)

@require_http_methods(['POST'])
@login_required(login_url='/login')
def edit_wishlist_ajax(request):
    id = request.POST['id']
    wishlistId = request.POST['reviewId']
    reason = request.POST['reason']
    wishlist = Wishlist.objects.filter(user=request.user, id=id).first()
    if wishlist is None:
        response = {
            "error": "Wishlist not found",
        }
        return HttpResponse(json.dumps(response), content_type='application/json')

    wishlist.reason = reason
    wishlist.save()

    response = {
        "id": id,
        "wishlistId": wishlistId,
        "reason": reason,
    }
    return HttpResponse(json.dumps(response), content_type='application/json')

@require_http_methods(['GET'])
@login_required(login_url='/login')
def get_wishlist_ajax(request):
    wishlist = (Wishlist.objects.values(
        'id',
        'book__id',
        'book__title',
        'book__image_url',
        'book__category',
        'reason',
    ).filter(user=request.user).all())
    wishlist = list(wishlist)
    print(wishlist)
    response = {
        "wishlist": wishlist,
    }
    return HttpResponse(json.dumps(response), content_type='application/json')

@require_http_methods(['POST'])
@login_required(login_url='/login')
def delete_wishlist_ajax(request, wishlist_id):
    wishlist = Wishlist.objects.filter(user=request.user, id=wishlist_id).first()
    if wishlist is None:
        response = {
            "error": "Wishlist not found",
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
    wishlist.delete()
    response = {
        "id": id,
        "message": "success delete wishlist"
    }
    return HttpResponse(json.dumps(response), content_type='application/json')
