from . import views
from django.urls import path

urlpatterns=[
          path('', views.property_view, name='home'),
          
]