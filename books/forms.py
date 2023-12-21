from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'book_image',
            'copies'
        ]

    
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    book_image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    copies = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

