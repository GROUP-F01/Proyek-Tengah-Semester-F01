import math
from django.shortcuts import render
from django.urls import reverse
from main.models import Buku
from .models import Review, ReviewSerializer
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from functools import wraps

def user_not_superuser(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrap

def show_review(request):
    buku = Buku.objects.all()
    review = Review.objects.all()
    context = {
        'kumpulanbuku': buku,
    }
    return render(request, "review.html", context)

def show_review_by_id(request, id):
    buku = Buku.objects.get(pk=id)
    context = {
        'buku': buku,
    }
    return render(request, "detail-review.html", context)

@login_required(login_url='/login')
@user_not_superuser
def show_users_review(request):
    buku = Buku.objects.all()
    user=request.user
    review = Review.objects.filter(user = user)
    context = {
        'user': user,
        'reviews' : review
    }
    return render(request, "my-review.html", context)

@api_view(('GET',))
def get_reviews_buku(request, id):
    data = Review.objects.filter(buku__id=id)
    review_serializer = ReviewSerializer(data,many=True)

    return Response(data=review_serializer.data)

def get_buku(request):
    buku = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', buku))

@csrf_exempt
def add_review_ajax(request, id):
    if request.user.is_staff == True:
        return render(request, 'login.html')
    if request.method == 'POST':
        user = request.user
        buku = Buku.objects.get(pk=id)
        rating = int(request.POST.get("rating"))
        review = request.POST.get("review")

        existing_review = Review.objects.filter(user=user, buku=buku).first()

        if existing_review:
            return HttpResponseBadRequest("Anda sudah menulis review untuk buku ini.")

        data = Review.objects.filter(buku__id=id)
        rata = (buku.rating*len(data) + rating)/(len(data)+1)
        rata = round(rata,2)
        rata = "{:.2f}".format(rata)
        buku.rating = rata
        buku.save()

        new_review = Review(user=user, buku=buku, rating=rating, review=review)
        new_review.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_review(request, id):
    review = Review.objects.get(pk = id)
    buku = review.buku
    id_buku = buku.pk
    rating = review.rating
    data = Review.objects.filter(buku__id=id_buku)
    if len(data)-1==0:
        rata = 0
    else:
        rata = (buku.rating*len(data) - rating)/(len(data)-1)
    rata = round(rata,2)
    rata = "{:.2f}".format(rata)
    buku.rating = rata
    buku.save()
    review.delete()
    return HttpResponseRedirect(reverse('review:user_reviews'))