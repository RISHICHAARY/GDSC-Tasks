from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('About',views.About,name='About'),
    path('Work',views.Work,name='Work'),
    path('Contact',views.Contact,name='Contact'),
]
