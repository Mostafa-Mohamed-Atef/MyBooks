from django.shortcuts import *
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import *
# Create your views here.
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account is successfully created')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')