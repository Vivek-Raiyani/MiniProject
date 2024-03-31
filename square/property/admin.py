from django.contrib import admin

from .models import Property, propertyImage,propertyLocation,currentrenter,typeOfProperty,propertyDocument,pricing

# Register your models here.
admin.site.register(Property)
admin.site.register(propertyLocation)
admin.site.register(currentrenter)
admin.site.register(typeOfProperty)
admin.site.register(propertyDocument)
admin.site.register(pricing)
admin.site.register(propertyImage)
