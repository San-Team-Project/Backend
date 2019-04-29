from django.contrib import admin
from django.conf import settings
from .models import Doctor,Specialization,DoctorType,Emergency,Settings,Venue
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','phone','specialization']
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name', 'email','phone')
    search_fields = ('name','specialization','city','country','hospital ')
    list_filter=['specialization','regadate','country','state']
    list_per_page = 18

class EmerAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'country','number']
    list_display_links = ('id','name', 'country','number')
    search_fields = ('name','number')
    list_filter=['name','number']
    list_per_page = 18

class DoctorTypee(admin.ModelAdmin):
    list_display = ['id','name',]
    list_display_links = ('id','name')
    search_fields = ('name','id')
    list_filter=[]
    list_per_page = 20

# @admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('..static/css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                '..static/js/admin/location_picker.js',
            )

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Specialization)
admin.site.register(DoctorType, DoctorTypee)
admin.site.register(Emergency,EmerAdmin)
admin.site.register(Settings)
admin.site.register(Venue,VenueAdmin)