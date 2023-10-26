from django.forms import ModelForm
from main.models import Buku

class ProductForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["isbn","title","description", "author", "publisher", "publication_date", "page_count", "category", "image_url", "lang", "price"]