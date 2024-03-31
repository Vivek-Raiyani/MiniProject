from django.shortcuts import render
from .models import Property, propertyImage, typeOfProperty, propertyLocation, currentrenter,pricing
from reviews.models import reviews, rating 
from booking.models import Booking, Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.

#  .filter method gives back query set

#  .get method gives back obkject

#  returns property,imah=ge, type object
def get_property_display(property_id):
    try:
        property_ = Property.objects.get(pk=property_id)
        print(property_)
        print()
        
        image_=propertyImage.objects.get(property=property_)
        print(image_)
        print()

        type_=typeOfProperty.objects.get(property=property_)
        print(type_)
        print()

        location_ = propertyLocation.objects.get(property=property_)

        return {
            'property': property_,
            'image': image_,
            'type': type_,
        }
    
    except Property.DoesNotExist:
        return None


# returns revies and rating of property
def get_reviews(property_id):
    property_=Property.objects.get(pk=property_id)
    reviews_ = reviews.objects.filter(property=property_)
    print(reviews_)
    #print()

    # Retrieve ratings for the property
    ratings_ =  rating.objects.filter(property=property_)
    print(ratings_)
    #print()
        
    return {
        'reviews': reviews_,
        'ratings': ratings_,
        }





def property_view(request, property_id):
    """
    View function to render the property detail page.
    """
    # Retrieve property info using the provided property_id
    place=get_property_display(property_id)
    print(place)
    reviews=get_reviews(property_id)
    print(reviews)

    if property:
        # If property info is found, render the detail page

         # property detials to be fetched like pricing, location etc
        return render(request, 'property/property.html', {'place': place, 'data': reviews})
    else:
        # If property info is not found, render a 404 page
        return render(request, '404.html', status=404)


# combine the booking and property page or keep them seperate?
    

'''
Your approach seems correct. However, it appears there's a typo in the code. In Django, the reverse relation is typically named using the lowercase name of the related model followed by "_set". Therefore, it should be propertyimage_set instead of propertyImage_set. Here's the corrected code:

python
Copy code
property = property_info['property']
images = property.propertyimage_set.all()
print(images)
Make sure to use the correct naming convention for the reverse relation. This should resolve the issue you're encountering. If you still face problems, ensure that the related models and their relations are correctly defined in your Django models.
'''

from datetime import datetime

def date_difference(date1, date2):
    # Convert the input strings to datetime objects
    date1_obj = datetime.strptime(date1, '%Y-%m-%d')
    date2_obj = datetime.strptime(date2, '%Y-%m-%d')

    # Calculate the difference between the two dates
    difference = date2_obj - date1_obj

    # Calculate the difference in days
    difference_days = difference.days

    # Calculate the difference in months
    difference_months = date2_obj.month - date1_obj.month + 12 * (date2_obj.year - date1_obj.year)

    # Calculate the difference in years
    difference_years = date2_obj.year - date1_obj.year

    return difference_days, difference_months, difference_years

    