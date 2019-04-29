from django.contrib import admin
from .models import Hospital
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
  list_display = ['name','phone','email', 'state', 'country']
  prepopulated_fields = {'slug': ('name',)}
  list_display_links=('state','country')
  # list_editable=['name','phone','email']
  list_filter=['name','country','state']
  search_fields = ('name','city','state','country')
  list_per_page= 10

admin.site.register(Hospital,HospitalAdmin)
