from django.urls import path
from . import views

urlpatterns=[
          path('', views.account, name='account'),
          path('add_property', views.add_property, name='add_property'),
          path('update', views.edit_profile, name='edit_profile'),
          path('remove_property', views.remove_property, name='remove_property'),
]