from django.urls import path
from . import views
app_name = 'wishlist'
urlpatterns=[
          path('', views.wishlist, name='wishlist'),
          path('add_to_wishlist/<int:property_id>/', views.add_to_wishlist, name='add_to_wishlist'),
          
]