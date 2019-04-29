from django.urls import path

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('contact/details/<int:pk>/', views.contact_detail, name='contact_detail'),
]