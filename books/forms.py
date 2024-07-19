from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'author_name',
            'book_year',
            'book_genre', 
            'page_number', 
            'finished_date',
            'book_cover'
        ]
        widgets = {
            'finished_date': forms.DateInput(attrs={'type':'date'}),
        }