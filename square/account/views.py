from django.shortcuts import render

from django.shortcuts import render
from reviews.models import reviews
from  property.models import Property, current_renter

from property.views import get_property_details

# Create your views here.



def account(request):
    """
    View function to render the user profile page.
    """
    user = request.user  # Assuming user is authenticated
    user_properties = Property.objects.filter(owner=user)
    user_renting= current_renter.objects.filter(user=user)
    user_reviews = reviews.objects.filter(user=user)
    
    properties_info = []  # List to hold property info dictionaries
    for property in user_properties:
        property_info = get_property_details(property.id)  # Retrieve detailed info for each property
        if property_info:
            properties_info.append(property_info)

    context = {
        'user': user,
        'user_properties': properties_info,
        'user_reviews': user_reviews,
        'user_renting': user_renting
    }
    return render(request, 'profile.html', context)
