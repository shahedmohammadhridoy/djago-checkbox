from django.contrib import admin
from django.urls import path
from checkbox.views import *

urlpatterns = [
    path('', index, name= 'index'),
    path('admin/', admin.site.urls),
]
