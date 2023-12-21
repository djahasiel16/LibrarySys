from django.shortcuts import render, redirect
from .forms import BookForm
from django.urls import reverse
from books.models import Book
from home import views
from django.contrib import messages

# Create your views here.
def book_form_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Book Added Successfully')
            return redirect(reverse("home"))

        else:
            form = BookForm()

        return render(request, 'book/create.html', {'form':form})
    else:
        return redirect(reverse('home'))

    
def update_view(request):
    if request.user.is_staff:
        books = Book.objects.all()
        return render(request, 'book/edit.html', {'books':books, 'update':True})
    else:
        return redirect(reverse('home'))

def book_update_form_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    update = True
    if form.is_valid():
        form.save()
        messages.success(request, 'Book Updated Successfully')
        return redirect(reverse(update_view))
    
    return render(request, 'book/create.html', {'form':form, 'update':update})


def book_delete_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    messages.success(request, 'Book Deleted Successfully')
    return redirect(reverse(update_view))