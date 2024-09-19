"""
URL configuration for MyBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views 
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base_home, name="base"),
    path('home/', views.home, name="home"),
    path('<int:pk>/', views.BookDetailsView.as_view(), name='details'),
    path('add/', views.Adding.as_view(), name="adding"),
    path('update/<int:book_id>', views.update, name='update'),
    path('delete/<int:book_id>', views.deleting, name='deleting'),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #they are already built in views you don't need to create a view for them
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
    path('profile/', user_views.profile, name='profile')

]

#for profile pictures 
urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
