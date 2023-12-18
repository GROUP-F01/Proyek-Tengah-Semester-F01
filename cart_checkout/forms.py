from django.forms import ModelForm
from cart_checkout.models import Checkout

class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        fields = ["nama_pembeli", "alamat"]