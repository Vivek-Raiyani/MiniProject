from django.shortcuts import render
from property.models import Property, pricing, propertyDocument, propertyImage, propertyLocation, typeOfProperty

def get_all_properties():
    """
    Function to retrieve all properties present in the database.
    """
    all_properties ={
        'properties': Property.objects.all(),
        'images': propertyImage.objects.all(),
        'location': propertyLocation.objects.all(),
        'type': typeOfProperty.objects.all(),
        'pricing': pricing.objects.all(),
        'document': propertyDocument.objects.all(),
        
    }
    return all_properties


# Create your views here.
def home(request):

    # need to pass all the retrived infomation from all property individually for easy acees 
    all_properties = get_all_properties()
    x=all_properties['images']
    properties=all_properties['properties']

    # in html code how to render all properties indivialiit reun loop on the context
    # for debuggin purpose

    for i in x:
        print(i.default_image.url)

    # context=all_properties try

    return render(request, 'home/homepage.html', {'properties': properties, 'images': x})