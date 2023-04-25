from django.urls  import path
from . import views

urlpatterns = [
    path('', views.index)   # this will open views.py and call the index function in it
]