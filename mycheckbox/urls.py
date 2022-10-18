from django.contrib import admin
from django.urls import path
from checkbox.views import *

urlpatterns = [
    path('', index, name= 'Index'),
    path('admin/', admin.site.urls),
    path('delete/', index)
]
