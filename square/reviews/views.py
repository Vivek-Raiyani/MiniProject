from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from property.models import Property
from .models import rating, reviews

# Create your views here.

# a user can only post one review and rating per property it it not currently implemented

@login_required
# create from to add review for property
def add_reviews(request, property_id):
          if request.method=='POST':
                  # service user is only showed the add review option
                  revw=reviews()
                  user=request.user
                  place=Property.objects.get(id=property_id)

                  revw.review=request.POST.get('review')
                  revw.user=user
                  revw.property=place

                  rated=rating()
                  rated.property=place
                  rated.user=user
                  rated.rating=request.POST.get('rating')
                  rated.save()

                  return render(request, 'property/property.hmtl')
          return render(request ,'reviews/addreview.html')

@login_required
# create from to add review for property
def update_reviews(request, reviews_id):
          if request.method=='POST':
                  # service user is only showed the add review option
                  revw=reviews.objects.get(id=reviews_id)
                  revw.review=request.POST.get('review')
                  rated=rating.objects.get(user=request.user)
                  rated.rating=request.POST.get('rating')
                  rated.save()
                  revw.save()

                  return render(request, 'property/property.hmtl')
          return render(request ,'reviews/addreview.html')

@login_required
# create from to add review for property
def remove_reviews(request, reviews_id):
          if request.method=='POST':
                  # service user is only showed the add review option
                  revw=reviews.objects.get(id=reviews_id)
                  rated=rating.objects.get(user=request.user)
                  rated.delete()
                  revw.delete()

                  return render(request, 'property/property.hmtl')
          return render(request ,'reviews/addreview.html')