from django.urls import path

from . import views

urlpatterns = [

    path('hospital/', views.hospital, name='hospital'),
    path('hospital/<listing_id>/', views.hospital_details, name='hospital_details'),

]