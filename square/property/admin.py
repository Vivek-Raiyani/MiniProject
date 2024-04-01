from django.contrib import admin

from .models import Property, propertyImage,propertyLocation,currentrenter,typeOfProperty,pricing

# Register your models here.
admin.site.register(Property)
admin.site.register(propertyLocation)
admin.site.register(currentrenter)
admin.site.register(typeOfProperty)
admin.site.register(pricing)
admin.site.register(propertyImage)
