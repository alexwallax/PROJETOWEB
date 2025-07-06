from django.contrib import admin
from django.urls import path

from todos.views import home #importar a views - home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
