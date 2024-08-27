"""
URL configuration for tpsdjango project.

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
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

import backoffice.views
import bookr.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', backoffice.views.index),
    path('backoffice', backoffice.views.index),
    path('backoffice/getProduct', backoffice.views.getProduct),
    path('bookr/getBooks', bookr.views.getBooks),
    path('api/', include('todo.urls')),
    path('blog/', include('blog.urls')),
    path('nlp/', include('nlp.urls')),
]
