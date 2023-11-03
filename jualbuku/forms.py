from django.forms import ModelForm
from main.models import Buku

class InputBuku(ModelForm):
    class Meta:
        model = Buku
        fields = ["title", "description", "author", "publisher", "image_url", 
                  "price", "lang", "category","page_count","publication_date","isbn"]