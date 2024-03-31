from django.shortcuts import render
from reviews.models import reviews
from  property.models import Property, currentrenter, propertyDocument, propertyImage, propertyLocation, typeOfProperty, pricing
from booking.models import Booking, Transaction
from django.contrib.auth.decorators import login_required

from property.views import get_property_display

# Create your views here.

def history(user):
    record=Booking.objects.filter(user=user)
    transaction=[]
    for record in record:
        transaction+=Transaction.objects.filter(booking=record).filter(status=1)
    
    return transaction


@login_required
def account(request):
    """
    View function to render the user profile page.
    """
    user = request.user  # Assuming user is authenticated
   
    #property=get_property_display()

    # getting user history
    user_history = history(user)

    context = {
        'user': user,
    }
   

    # for debugging purpose to print details on the terminal
    
    
    
    return render(request, 'account/profile.html', context)

@login_required
def add_property(request):
    if request.user.user_type == 2:
        if request.method =='POST':
            property=Property()
            property.title=request.POST.get('title')
            property.availabality=True
            property.description=request.POST.get('description')
            property.user_preference=request.POST.get('user_preference')
            property.owner=request.user
            property.save()

            images=propertyImage()
            images.default_image=request.FILES.get('default_image')
            images.image2=request.FILES.get('image2')
            images.image3=request.FILES.get('image3')
            images.image4=request.FILES.get('image4')
            images.image5=request.FILES.get('image5')
            images.property=property
            images.save()

            document=propertyDocument()
            document.default_document=request.FILES.get('document')
            document.property=property
            document.save()

            location=propertyLocation()
            location.location=request.POST.get('location')
            location.city=request.POST.get('city')
            location.state=request.POST.get('state')
            location.country=request.POST.get('country')
            location.zipcode=request.POST.get('pincode')
            location.property=property
            location.save()
            
            type=typeOfProperty()
            type.property_type=request.POST.get('property_type')
            type.property=property
            type.save()

            price=pricing()
            price.price=request.POST.get('price')
            price.price_type=request.POST.get('price_type')
            price.property=type
            price.save()
            return render(request, 'account/profile.html')

        return render(request, 'account/add_property.html')

    return render(request, 'account/profile.html')


# implement by use of button not changing url
#version1
@login_required
def remove_property(request):
    if request.user.user_type == 2:
        if request.method == 'POST':
            property_id = request.POST.get('property_id')
            property = Property.objects.get(id=property_id)
            property.delete()
            return render(request, 'account/profile.html')

        return render(request, 'account/remove_property.html')
    
    return render(request, 'account/profile.html')

#version 2-----using button not chaning url need to be implemented currently is not working
def remove_property(request, property_id):
    if request.user.user_type == 2:
        if request.method == 'POST':
            property = Property.objects.get(id=property_id)
            property.delete()
            return render(request, 'account/profile.html')

        return render(request, 'account/remove_property.html')
    
    return render(request, 'account/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        #user.email = request.POST.get('email')
        #user.phone_no = request.POST.get('phone_no')
        #user.gender = request.POST.get('gender')
        #user.user_type = request.POST.get('user_type')
        #user.first_name = 'first_name'
        #user.last_name = 'last_name'

        if request.FILES.get('profile_pic'):
            pic=request.FILES.get('profile_pic')
            print(pic)
            print(request.FILES.get('profile_pic'))
            user.profile_pic.delete()
            user.profile_pic = pic
        

        user.save()
        return render(request, 'account/profile.html')
    return render(request, 'account/edit_profile.html')


# Create your views here.


# similar to home page but need to extract from the wish list table all same

def get_properties(user):
    """
    Function to retrieve all properties in the wishlist of the current user.
    """
    try:
        # Retrieve wishlist items for the current user
        properties = Property.objects.filter(owner=user)

        # Extract property objects from wishlist items
        return properties

    except properties.DoesNotExist:
        return []
    

@login_required
def myproperty(request):
    """
    View function to render the wishlist page for the current user.
    """
    if request.user.is_authenticated:
        user = request.user
        properties = get_properties(user)

        
        # printing all the wishlist propert on the terminal for debuggin puropse
        print(user)
            



        return render(request, 'account/myproperty.html', {'properties': properties })
    else:
        # Handle case where user is not authenticated
        return render(request, 'account/myproperty.html', {'properties': []})
    
def get_rent(user):
    property_id=currentrenter.objects.filter(user=user)
    property=[]
    booking=[]
    for id in property_id:
        property.append(Property.objects.get(id=id.property_id))
        booking.append(Booking.objects.get(property=id.property_id))
    return {
        'property': property,
        'booking': booking
    }

def myrental(request):
    if request.user.is_authenticated:
        user = request.user
        properties = get_rent(user)
        print(properties)
        return render(request, 'account/myrental.html', {'properties': properties })
    else:
        # Handle case where user is not authenticated
        return render(request, 'account/myrental.html', {'properties': []})