from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
  path('doctor', views.DoctorList.as_view(), name ='adoctor'),
  path('doctor/<int:pk>/', views.DoctorDetails.as_view(), name ='detail'),

  path('doctorr', views.ddoctorList, name ='ddoctor'),
  path('doctorr/<int:pk>/', views.ddoctorDetails, name ='ddetail'),
]