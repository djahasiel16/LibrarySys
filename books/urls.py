from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.book_form_view, name='create_book'),
    path('update/', views.update_view, name='update'),
    path('update/<book_id>/', views.book_update_form_view, name='update_book'),
    path('delete/<book_id>/', views.book_delete_view, name='delete_book'),
]