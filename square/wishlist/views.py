from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

        # Extract property objects from wishlist items
        return wishlist_properties

    except Wishlist.DoesNotExist:
        return []
    

@login_required
def wishlist(request):
    """
    View function to render the wishlist page for the current user.
    """
    if request.user.is_authenticated:
        user = request.user
        wishlist_properties = get_wishlist_properties(user)

        
        # printing all the wishlist propert on the terminal for debuggin puropse
        print(user)
        print(wishlist_properties)


        return render(request, 'wishlist/wishlist.html', {'wishlist_properties': wishlist_properties})
    else:
        # Handle case where user is not authenticated
        return render(request, 'wishlist/wishlist.html', {'wishlist_properties': []})