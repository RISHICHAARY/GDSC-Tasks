from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('Post',views.Post,name='Post'),
]
