from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from django.urls import reverse
# Create your models here.

MY_CHOICES = (('Private', 'Private'),
              ('Public', 'Public'),
              ('Clinic', 'Clinic'))

class Hospital(models.Model):
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, unique=True ,db_index=True)
  email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
  phone = models.CharField(max_length=20)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default="noimage.png")
  photourl = models.URLField(blank = True, null = True)
  about = HTMLField()
  hospitallink = models.URLField(blank = True, null = True)
  timing = HTMLField()
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=20)
  state= models.CharField(max_length=20)
  country= models.CharField(max_length=20)
  type = models.CharField(max_length=100, choices=MY_CHOICES,default='public')
  regadate = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name

  def __unicode__(self):
      return self.name

  def get_absolute_url(self):
      return reverse('hospital_details', args=[self.slug])