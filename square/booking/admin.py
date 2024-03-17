from django.contrib import admin
from .models import Booking,Transaction,cancalation

# Register your models here.
admin.site.register(Booking)
admin.site.register(Transaction)
admin.site.register(cancalation)