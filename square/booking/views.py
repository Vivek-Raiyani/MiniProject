from django.shortcuts import redirect, render
from django.urls import reverse   
from .models import Booking, Transaction, cancalation 
from django.contrib.auth.decorators import login_required
from property.models import Property,currentrenter

# Create your views here.

@login_required
def booking(request):# pass property id as a parameter
          if request.method == 'POST':
                    #creating a booking record
                    booking=Booking()
                    booking.user = request.user
                    place=Property.objects.get(id=request.POST.get('property'))
                    booking.property = place
                    booking.start_date = request.POST.get('start_date')
                    booking.end_date = request.POST.get('end_date')
                    booking.amount = request.POST.get('amount')
                    booking.save()

                    # creating transaction record
                    record=Transaction()
                    record.booking = booking
                    record.status = 3
                    record.save()

                    place.availabality= False
                    place.times_rented+=1
                    place.save()

                    renter=currentrenter.objects.create(property=place,user=booking.user)
                    renter.save()

                    

                    return render(request, 'account/profile.html')
          return render(request, 'booking/booking.html')

@login_required
def cancle(request,booking_id):
        book = Booking.objects.get(id=booking_id)
        print(book)
        print("hii")
        print(book.was_cancled)
        if book.was_cancled == False:
               book.was_cancled = True
               print(book.was_cancled)
               book.save()
        if book.was_cancled == True:
                renter = currentrenter.objects.get(user=book.user, property=book.property)
                print('heelo')
                print(renter)
                renter.delete()
            
        return redirect(reverse('account:myrental'))
    
def history(request):
    record=Booking.objects.filter(user=request.user)
    print(record)
    return render(request, 'booking/history.html', {'record': record})