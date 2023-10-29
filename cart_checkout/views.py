from django.shortcuts import render, redirect
from main.models import Buku
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from cart_checkout.forms import CheckoutForm
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def init_cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}

def add_to_cart(request, book_id):
    if request.method == "POST":
        buku = Buku.objects.get(pk=book_id)
        

        cart=request.session.get('cart', {})
        cart[book_id]=buku.title
        request.session['cart'] = cart

        total_price = request.session.get('total_price', 0)
        total_price += buku.price
        request.session['total_price'] = total_price

        amount_added = request.session.get('amount_added', 0)
        request.session['amount_added'] = amount_added + 1

    return redirect('main:show_main')

def book_checkout(request):
    form = CheckoutForm(request.POST or None)
    cart = request.session.get('cart',{})
    total_price = request.session.get('total_price', 0)

    if form.is_valid() and request.method == "POST":

        form.save()

        book_titles = list(cart.values())

        checked_out_titles = request.session.get('checked_out_titles', [])
        checked_out_titles.extend(book_titles)
        request.session['checked_out_titles'] = checked_out_titles

        request.session['cart']= {}
        request.session['amount_added'] = 0
        request.session['total_price'] = 0



        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form, 
        'cart': cart,
        'total_price': total_price
        }
    
    return render(request, "checkout.html", context)

def inventory(request):
    checked_out_titles = request.session.get('checked_out_titles', [])

    context = {
        'book_titles': checked_out_titles,
    }

    return render(request, 'inventory.html', context)

def delete_book(request, book_title):
    checked_out_titles = request.session.get('checked_out_titles', [])
    if book_title in checked_out_titles:
        checked_out_titles.remove(book_title)
        request.session['checked_out_titles'] = checked_out_titles

    return HttpResponseRedirect(reverse('cart_checkout:inventory'))

@csrf_exempt
def delete_book_ajax(request, book_title):
    if request.method == 'DELETE':
        checked_out_titles = request.session.get('checked_out_titles', [])
        if book_title in checked_out_titles:
            checked_out_titles.remove(book_title)
            request.session['checked_out_titles'] = checked_out_titles
            return HttpResponse(b"DELETED", status=200)
        else:
            return HttpResponseNotFound()
    return HttpResponseNotFound()

