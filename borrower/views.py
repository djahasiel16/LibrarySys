from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book
from .models import BorrowedBook
from django.contrib.auth.models import User
from django.contrib import messages
import inflect


# Create your views here.
def borrower_view(request, user_id, book_id):
   
    book = Book.objects.get(pk=book_id)
    user = User.objects.get(pk=user_id)

    try:
        b_book = BorrowedBook.objects.get(user=user, borrowed_book=book)
        b_book.borrowed_copies += 1
        book.copies -= 1

        book.save()
        b_book.save()
    except:
        borrower = BorrowedBook(user=user, borrowed_book=book, borrowed_copies=1)
        book.copies -=1

        book.save()
        borrower.save()        

    messages.success(request, "Book Borrowed Successfully")
    return redirect(reverse('books_page'))

def book_history_view(request):
    borrowed_books = BorrowedBook.objects.filter(user=User.objects.get(pk=request.user.id))
    
    return render(request, 'borrower/book_history.html', {'book_borrower':borrowed_books, 'notEmpty':borrowed_books.exists()})


def borrower_book_management(request):    
    user = User.objects.get(pk=request.user.id)
    borrowed_books = BorrowedBook.objects.filter(user=user, borrowed_copies__gt=0)
    p = inflect.engine()
    numbers = [p.number_to_words(i) for i in range(1,len(borrowed_books) + 1)]
    books_numbers = zip(borrowed_books, numbers)

    context = {'book_borrower':books_numbers, 'notEmpty':borrowed_books.exists()}
    
    return render(request, 'borrower/borrower_book_management.html', context)

    
def return_a_copy(request, borrower_id):
    book_borrower = BorrowedBook.objects.get(pk=borrower_id)
    book = Book.objects.get(pk=book_borrower.borrowed_book.id)
    book_borrower.borrowed_copies -= 1
   
    book.copies += 1
    book.save()
    book_borrower.save()

    messages.success(request, "A Copy Returned Successfully")

    return redirect(reverse(borrower_book_management))

def return_all_copies(request, borrower_id):
    book_borrower = BorrowedBook.objects.get(pk=borrower_id)
    book = Book.objects.get(pk=book_borrower.borrowed_book.id)
    book_borrower.borrowed_copies = 0
   
    book.copies += book_borrower.borrowed_copies
    book.save()
    book_borrower.save()

    messages.success(request, "All Copies Returned Successfully")

    return redirect(reverse(borrower_book_management))