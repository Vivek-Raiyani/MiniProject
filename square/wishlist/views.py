
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from property.models import Property
from django.contrib import messages


from .models import Wishlist

# Create your views here.


# similar to home page but need to extract from the wish list table all same

def get_wishlist_properties(user):
    """
    Function to retrieve all properties in the wishlist of the current user.
    """
    try:
        # Retrieve wishlist items for the current user
        wishlist_properties = Wishlist.objects.filter(user=user).select_related('property')
        
        if not wishlist_properties:
            return None
        # Extract property objects from wishlist items
        return wishlist_properties

    except Wishlist.DoesNotExist:
        return None
    

@login_required
def wishlist(request):
    """
    View function to render the wishlist page for the current user.
    """
    if request.user.is_authenticated:
        user = request.user
        wishlist_properties = get_wishlist_properties(user)

        # printing all the wishlist propert on the terminal for debuggin puropse

        if wishlist_properties is None:
            messages.info(request, 'No properties found in wishlist.')
            return render(request, 'wishlist/wishlist.html', {'wishlist_properties': []})


        return render(request, 'wishlist/wishlist.html', {'wishlist_properties': wishlist_properties})
    else:
        # Handle case where user is not authenticated
        return render(request, 'wishlist/wishlist.html', {'wishlist_properties': []})
    
def add_to_wishlist(request, property_id):
    """
    View function to add a property to the wishlist of the current user.
    """
    if request.user.is_authenticated:
        user = request.user
        property = Property.objects.get(id=property_id)
        if user==property.owner:
            return redirect('property:view', property_id=property_id)
        if Wishlist.objects.filter(user=user, property=property).exists():
            return redirect('wishlist:wishlist')
        # Create a new wishlist item
        wishlist_item = Wishlist(user=user, property=property)
        # Save the wishlist item
        wishlist_item.save()
      

        return redirect('wishlist:wishlist')
    else:
        return render(request, 'wishlist/wishlist.html', {'message': 'You must be logged in to add to wishlist.'})