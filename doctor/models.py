from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
from tinymce.models import HTMLField
from django.utils import timezone
from django.urls import reverse
# from django.core.validators import email_re
# from django.core.exceptions import ValidationError
# Create your models here.
from .choices import MY_CHOICES

class Specialization(models.Model):
  id = models.AutoField(primary_key=True)
  details = HTMLField()

  def __str__(self):
    return self.details

class DoctorType(models.Model):
  id = models.AutoField(primary_key=True)
  name = HTMLField()

  def __str__(self):
    return self.name

class Emergency(models.Model):
  id = models.AutoField(primary_key=True)
  country = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  number = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

  def __str__(self):
    return self.name

class Doctor(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, unique=True ,db_index=True)
  email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
  phone = models.CharField(max_length=20)
  specialization = models.CharField(max_length=100, choices=MY_CHOICES,default='Cardiologist')
  #specialization =MultiSelectField(choices=MY_CHOICES)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  about = HTMLField()
  documents = models.FileField(upload_to='photos/%Y/%m/%d/', default="img.pdf")
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=20)
  state= models.CharField(max_length=20)
  country= models.CharField(max_length=20)
  hospital = models.CharField(max_length=150)
  hospitallink = models.URLField(blank = True, null = True)
  portfoliolink = models.URLField(blank = True, null = True)
  availabel = models.CharField(max_length=200, default="MON-FRI: 9:00 - 18:00 ")
  timing = HTMLField()
  experiance = models.IntegerField()
  verified = models.BooleanField(default=False)
  regadate = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name

  def __unicode__(self):
      return self.id

  def save(self, *args, **kwargs):
    if self.email is not None and self.email.strip() == "":
        self.email = None
    models.Model.save(self, *args, **kwargs)


  def get_absolute_url(self):
      return reverse('doctor_details', args=[self.slug])


class Settings(models.Model):
  receive_newsletter = models.BooleanField()
  
  def __str__(self):
    return self.receive_newsletter


class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)


