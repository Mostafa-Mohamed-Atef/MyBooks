from django.shortcuts import *
from django.http import *
from .models import Book
from django.http import *
from django.template import *
from .forms import BookForm
from django.contrib import messages
from django.views.generic import *
from django.contrib.auth.decorators import *
# Create your views here.
# def home(request):
#     book_list = Book.objects.all()
#     context = {
#         'book_list': book_list,
#     }
#     return render(request, 'books/home.html', context)

class IndexClassView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'book_list'

#for book details 
# def details(request, book_id):
#     book = Book.objects.get(id=book_id)
#     context = {
#         'book':book,
#     }
#     return render(request, 'books/details.html', context)

class BookDetailsView(DetailView):
    model = Book
    template_name = 'books/details.html'

#for adding books
# def adding(request):
#     form = BookForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     context={
#         'form':form
#     } 
#     return render(request, "books/forms.html", context)

class Adding(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/forms.html'
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    

#for updating books values
def update(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully")
        return redirect('home')
    context = {
        'book':book,
        'form': form,
    }
    return render(request, 'books/forms.html', context)
#for deleting a book
def deleting(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Deleted Successfully")
        return redirect('home')
    
    return render(request, 'books/home.html', {'book':book})