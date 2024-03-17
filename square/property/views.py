from django.shortcuts import render

# Create your views here.
def property(request):
          return render(request,'property/property.html')