from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def register(request):
    form = UserChangeForm()
    return render(request, 'users/register.html', {'form': form})