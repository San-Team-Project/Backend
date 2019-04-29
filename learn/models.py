from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    bio = models.TextField(max_length=500)


# class Country(models.Model):
#   name = models.CharField(max_length=30)

#   def __str__(self):
#     return self.name

# class City(models.Model):
#   country = models.ForeignKey(Country, on_delete=models.CASCADE)
#   name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name


# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     birthdate = models.DateField(null=True, blank=True)
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.name