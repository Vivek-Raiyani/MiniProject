from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from property.models import Property
from django.urls import reverse
from .models import rating, reviews

# Create your views here.

# a user can only post one review and rating per property it it not currently implemented

@login_required
# create from to add review for property
def add_reviews(request):
          if request.method=='POST':
                  # service user is only showed the add review option
                  revw=reviews()
                  user=request.user
                  #place=Property.objects.get(id=property_id)
                  place=Property.objects.get(id=request.POST.get('property'))

                  revw.review=request.POST.get('review')
                  revw.user=user
                  revw.property=place

                  rated=rating()
                  rated.property=place
                  rated.user=user
                  rated.rating=request.POST.get('rating')
                  rated.save()

                  revw.save()

                  return redirect(reverse('property:property',args=[place.id]))
          return render(request ,'reviews/add_reviws.html')

@login_required
# create from to add review for property
def update(request, reviews_id,rating_id):
          
          if request.method=='POST':
                  # service user is only showed the add review option
                  revw=reviews.objects.get(id=reviews_id)
                  revw.review=request.POST.get('review')
                  rated=rating.objects.get(id=rating_id)
                  rated.rating=request.POST.get('rating')
                  rated.save()
                  revw.save()

                  return redirect(reverse('property:property',args=[revw.property.id]))
          return render(request ,'reviews/addreview.html')

@login_required
# create from to add review for property
def remove(request, reviews_id,rating_id):
          if request.method=='POST':
                  # service user is only showed the add review option
                  revw=reviews.objects.get(id=reviews_id)
                  rated=rating.objects.get(id=rating_id)
                  rated.delete()
                  revw.delete()

                  return redirect(reverse('property:property',args=[revw.property.id]))
          return render(request ,'reviews/addreview.html')