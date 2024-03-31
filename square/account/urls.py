from django.urls import path
from . import views

app_name='account'
urlpatterns=[
          path('', views.account, name='profile'),
          path('add_property', views.add_property, name='add_property'),
          path('update', views.edit_profile, name='edit_profile'),
          path('remove_property', views.remove_property, name='remove_property'),
          path('myproperty', views.myproperty, name='myproperty'),
          path('myrental', views.myrental, name='myrental'),
]