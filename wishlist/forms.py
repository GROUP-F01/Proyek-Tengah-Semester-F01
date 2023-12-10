from django.forms import ModelForm, forms, ModelChoiceField
from main.models import Buku
from .models import Wishlist

class WishlistForm(ModelForm):
    book = ModelChoiceField(queryset=Buku.objects.all(), empty_label="Select a book", to_field_name="title")
    class Meta:
        model = Wishlist
        fields = ['book', 'reason']