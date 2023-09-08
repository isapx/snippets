
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #name = home es el nombre que uso para invocarlo desde los html ejem en un link
    path('add_snippet/',views.add_snippet, name ='add_snippet'),
    
]
