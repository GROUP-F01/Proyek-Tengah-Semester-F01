from django.urls import path
from .views import show_review, show_review_by_id, add_review_ajax, get_reviews_buku, get_buku, show_users_review, delete_review

app_name = 'review'

urlpatterns = [
    path('review/', show_review, name='show_review'),
    path('review/<int:id>/', show_review_by_id, name='show_review_by_id'),
    path('add-review/<int:id>/', add_review_ajax, name='add_review'),
    path('get-review/<int:id>/', get_reviews_buku, name='get_reviews'),
    path('my-review/', show_users_review, name='user_reviews'),
    path('get-buku/', get_buku, name = 'get_buku'),
    path('delete/<int:id>', delete_review, name='delete_review'),
]
