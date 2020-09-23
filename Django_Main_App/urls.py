"""Django_Main_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from PMS_APP.views import home , register , login , profile , logout , edit_pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name = 'home'),
    path('register', register , name = 'register'),
    path('login', login , name = 'login'),
    path('profile', profile , name = 'profile'),
    path('logout', logout , name = 'logout'),
    path('edit_pass', edit_pass , name = 'edit_pass'),






]


# Important
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

