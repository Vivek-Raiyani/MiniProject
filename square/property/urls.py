from . import views
from django.urls import path
app_name = 'property'
urlpatterns=[
          path('<int:property_id>/', views.property_view, name='view'),
          path('remove/<int:property_id>/', views.remove_property, name='remove'),
          
]