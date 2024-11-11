from django.urls import path
from boostrapApp import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.service, name='services'),

]