from django.urls import path
from . import views

urlpatterns = [
    path('',views.app,name='index'),
    path('about',views.appabt,name='about')
    path('contact',views.contact,name='Ccontact')
]