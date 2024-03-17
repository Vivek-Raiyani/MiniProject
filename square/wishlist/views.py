from django.shortcuts import render

# Create your views here.
def wishlist(request):
          return render(request,'wishlist/Base.html')

# similar to home page but need to extract from the wish list table all same