from django.shortcuts import render
from .models import Property, propertyImage, typeOfProperty, propertyLocation, current_renter
from reviews.models import reviews, rating 
from booking.models import Booking, Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.



def get_property_details(property_id):
    """
    Function to retrieve all data related to a particular property from the database.
    """
    try:
        # Retrieve the property object
        property_obj = Property.objects.get(pk=property_id)

        # Retrieve reviews for the property
        property_reviews = reviews.objects.filter(property=property_obj)

        # Retrieve ratings for the property
        property_ratings = rating.objects.filter(property=property_obj)

        # Retrieve property images
        property_images = propertyImage.objects.filter(property=property_obj)

        # Retrieve type of property
        property_type = typeOfProperty.objects.filter(property=property_obj).first()

        # Retrieve property location
        property_location = propertyLocation.objects.filter(property=property_obj).first()

        # Retrive current renter
        if not property_obj.availabality:
            current_renter=current_renter.objects.filter(property=property_obj).first()
        else:
            current_renter = None

        # Prepare a dictionary containing all the retrieved data
        property_details = {
            'property': property_obj,
            'reviews': property_reviews,
            'ratings': property_ratings,
            'images': property_images,
            'type': property_type,
            'location': property_location,
            'current_renter': current_renter
        }


        return property_details

    except Property.DoesNotExist:
        return None


def property_view(request, property_id):
    """
    View function to render the property detail page.
    """
    # Retrieve property info using the provided property_id
    property_info = get_property_details(property_id)

    property=property_info['property']
    image=property.propertyimage_set.all()
    print(image)
    for i in image:
        print(i.default_image.url)


    # pass all the object with details use the functions to do it

    if property_info:
        # If property info is found, render the detail page

         # property detials to be fetched like pricing, location etc
        return render(request, 'property/property.html', {'property': property, 'image':image})
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
    