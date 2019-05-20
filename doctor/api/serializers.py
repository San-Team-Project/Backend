from rest_framework import serializers
from doctor.models import Doctor,Specialization,Emergency, DoctorType
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


# This is Doctor Section Api 

class TypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DoctorType
    fields = ('pk','name')


class ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = ('pk','name','slug','email','phone','specialization','photo',
              'timing','state','country','about','address','city','hospital',
              'hospitallink','portfoliolink','availabel','experiance')

# class DetailSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Doctor
#     fields = ('pk','name','slug','email','phone','specialization','photo',
#               'timing','state','country','about','address','city','hospital',
#               'hospitallink','portfoliolink ','availabel','experiance')


class PListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = ('pk','name','slug','email','phone','specialization','photo',
              'timing','state','country','availabel','regadate')

class DetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = ('pk','name','slug','email','phone','specialization','photo',
              'timing','state','country','about','address','city','hospital',
              'hospitallink','portfoliolink','availabel','experiance','regadate')


# This is End Of Doctor  Section Api 

class AlistSerializer(serializers.ModelSerializer):
  class Mets:
    model = Specialization
    fields = ('pk','details')