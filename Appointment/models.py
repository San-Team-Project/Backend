from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
class Appointment(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  time = models.CharField(max_length=100)
  date = models.DateTimeField(default=datetime.now, blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('appointment_details', args=[self.pk])