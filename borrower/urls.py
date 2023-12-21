from django.urls import path
from . import views

urlpatterns = [
    path('borrow/<user_id>/<book_id>/', views.borrower_view, name='borrow_book'),
    path('history/', views.book_history_view, name='book_history'),
    path('borrowed_book_management/', views.borrower_book_management, name='borrower_book_management'),
    path('return_a_copy/<borrower_id>/', views.return_a_copy, name='return_a_copy'),
    path('return_all_copies/<borrower_id>/', views.return_all_copies, name='return_all_copies'),
]