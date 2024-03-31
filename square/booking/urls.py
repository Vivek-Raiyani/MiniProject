from django.urls import path
from . import views

app_name='booking'
urlpatterns=[
          path('', views.booking, name='booking'),
          path('history/', views.history, name='history'),
          path('cancalation/<int:booking_id>/', views.cancle, name='cancle'),
          
]