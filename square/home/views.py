from django.shortcuts import render
from property.models import Property



# Create your views here.
def home(request):

    # need to pass all the retrived infomation from all property individually for easy acees

    all_properties = Property.objects.prefetch_related('propertyimage_set', 'propertylocation_set').all()
    

    # in html code how to render all properties indivialiit reun loop on the context
    # for debuggin purpose

    # context=all_properties try

    # remove the image table and other non necessat table if poasible

    return render(request, 'home/homepage.html', {'properties': all_properties})