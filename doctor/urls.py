from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('geo/', views.geo, name='geo'),
    path('doctor/', views.doctor, name='doctor'),
    path('adddoctor/', views.adddoctor, name='doctoradd'),
    path('doctor/<listing_id>/', views.doctor_detail, name='doctor_details'),
    

]