from django.urls import path
from . import views
app_name='reviews'
urlpatterns=[
          path('', views.add_reviews, name='reviews'),  
          path('update/',views.update, name='update') ,
          path('remove/',views.remove,name='remove')       
]