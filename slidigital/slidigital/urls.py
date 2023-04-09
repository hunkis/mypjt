"""
URL configuration for mysite project.

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
from django.urls import include, path
from django.shortcuts import redirect
from django.contrib import admin

urlpatterns = [
    path('', lambda request: redirect('randing/')),  # 루트 URL에 접속 시 'randing/'으로 redirect
    path('randing/', include('randing.urls')),
    path('result/', include('randing.urls')),
    path('statics/', include('randing.urls')),
    path('admin/', admin.site.urls),
]



