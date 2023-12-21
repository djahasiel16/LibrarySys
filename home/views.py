from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book
from borrower.models import BorrowedBook
from django.utils import timezone

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        current_date = timezone.now().date()
        
        b_books = BorrowedBook.objects.filter(date_borrowed__date=current_date)
        return render(request, 'home/home.html', {'b_books':b_books})
    else:
        return redirect(reverse('login'))
    
def book_views(request):
    books = Book.objects.all()
    return render(request, 'home/books.html', {'books':books})