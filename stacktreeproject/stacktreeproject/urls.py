"""stacktreeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name = 'main'),
    path('result/', main.views.result, name = 'result'),
    path('account/', include('account.urls')),
<<<<<<< HEAD
    path('position_detail/', main.views.position_detail, name = 'position_detail'),
=======
    path('mypage/', main.views.mypage, name = 'mypage'),
>>>>>>> 6229d492e89ae84a77142cbb9326f1b36f2ddf48
]
