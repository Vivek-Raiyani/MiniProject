from django.shortcuts import render
from reviews.models import reviews
from  property.models import Property, currentrenter, propertyImage, propertyLocation, typeOfProperty, pricing
from booking.models import Booking, Transaction
from django.contrib.auth.decorators import login_required


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

            images=propertyImage()
            images.default_image=request.FILES.get('default_image')
            images.image2=request.FILES.get('image2')
            images.image3=request.FILES.get('image3')
            images.image4=request.FILES.get('image4')
            images.image5=request.FILES.get('image5')
            images.property=property


            location=propertyLocation()
            location.location=request.POST.get('location')
            location.city=request.POST.get('city')
            location.state=request.POST.get('state')
            location.country=request.POST.get('country')
            location.zipcode=request.POST.get('pincode')
            location.property=property
            
            type=typeOfProperty()
            type.property_type=request.POST.get('property_type')
            type.property=property

            price=pricing()
            price.price=request.POST.get('price')
            price.price_type=request.POST.get('price_type')
            price.property=type


            property.save()
            images.save()
            location.save()
            type.save()
            price.save()
            return render(request, 'account/profile.html')

        return render(request, 'account/add_property.html')

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
    print(user)
    property_id = currentrenter.objects.filter(user=user)
    print(property_id)
    property = []
    booking = []
    print(property_id)

    if property_id:  # Check if property_id list is not empty
        print('hello')
        for id in property_id:
            property.append(Property.objects.get(id=id.property_id))
            book=Booking.objects.filter(property=id.property_id)
            print(book)
            for b in book:
                if b.was_cancled == False:
                    booking.append(b)
                    print(b)
                else:
                    print('was cancled')
    else:
        return None
    print(booking)
    return {
        'property': property,
        'booking': booking
    }

@login_required
def myrental(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        properties = get_rent(user)
        print('prop')
        print(properties)
        if properties is None:
            print("message")
            return render(request, 'account/myrental.html', {'message': 'No rentals found.'})
        return render(request, 'account/myrental.html', {'properties': properties })
    else:
        # Handle case where user is not authenticated
        return render(request, 'account/myrental.html', {'properties': []})