from django.contrib import admin

from .models import Property,propertyLocation,current_renter,typeOfProperty,propertyDocument,pricing

# Register your models here.
admin.site.register(Property)
admin.site.register(propertyLocation)
admin.site.register(current_renter)
admin.site.register(typeOfProperty)
admin.site.register(propertyDocument)
admin.site.register(pricing)
