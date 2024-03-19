from django.shortcuts import render

from django.shortcuts import render
from reviews.models import reviews
from  property.models import Property, current_renter, propertyDocument, propertyImage, propertyLocation, typeOfProperty, pricing
from booking.models import Booking, Transaction
from django.contrib.auth.decorators import login_required

from property.views import get_property_details

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
    user_properties = Property.objects.filter(owner=user)
    user_renting= current_renter.objects.filter(user=user)
    user_reviews = reviews.objects.filter(user=user)
    
    properties_info = []  # List to hold property info dictionaries
    for property in user_properties:
        property_info = get_property_details(property.id)  # Retrieve detailed info for each property
        if property_info:
            properties_info.append(property_info)

    # getting user history
    user_history = history(user)

    context = {
        'user': user,
        'user_properties': properties_info,
        'user_reviews': user_reviews,
        'user_renting': user_renting,
        'user_history': user_history
    }

    # for debugging purpose to print details on the terminal
    print(user)
    print(user_properties)
    print(user_reviews)
    print(user_renting)
    print(properties_info)
    print(context)
    print(user.profile_pic.url)
    print('user history')
    print(user_history)
    
    
    
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
            document.document=request.FILES.get('document')
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
            type.property_type=request.POST.get('type')

            price=pricing()
            price.price=request.POST.get('price')
            price.type=request.POST.get('price_type')
            price.property=property
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
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone_no = request.POST.get('phone_no')
        user.gender = request.POST.get('gender')
        user.user_type = request.POST.get('user_type')
        user.save()
        return render(request, 'account/profile.html')
    return render(request, 'account/edit_profile.html')