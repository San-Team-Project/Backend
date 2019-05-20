from django.urls import path

from . import views

urlpatterns = [
  path('appointment', views.appointment, name='appointment'),
  path('appointment/details/<int:pk>/', views.appointment_details, name='appointment_details'),
]