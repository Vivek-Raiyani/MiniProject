from django.shortcuts import render
from property.models import Property

def get_all_properties():
    """
    Function to retrieve all properties present in the database.
    """
    all_properties = Property.objects.all()
    return all_properties


# Create your views here.
def home(request):
    all_properties = get_all_properties()
    return render(request, 'home/Base.html', {'properties': all_properties})