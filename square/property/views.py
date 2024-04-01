from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Property, propertyImage, typeOfProperty, propertyLocation, currentrenter,pricing
from reviews.models import reviews, rating 
from booking.models import Booking, Transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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



def remove_property(request, property_id):  # Add property_id parameter
    if request.method == 'POST':
        print(property_id)
        property = Property.objects.get(id=property_id)
        print(property)
        if property.availabality == False:
            messages.error(request, 'Cannot delete property with active booking')
            print('Cannot delete property with active booking')
            return redirect(reverse('property:view',kwargs={'property_id': property_id}))  # Redirect to the user's profile page
        property.delete()
        print('deleted')
        return redirect(reverse('account:myproperty'))  # Redirect to the user's profile page
    return redirect(reverse('property:view',kwargs={'property_id': property_id}))  # Return a response for other HTTP methods
