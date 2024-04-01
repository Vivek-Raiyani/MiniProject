from django.shortcuts import redirect, render
from django.urls import reverse

from booking.mail import send_email   
from .models import Booking, Transaction, cancalation 
from django.contrib.auth.decorators import login_required
from property.models import Property,currentrenter
from django.contrib import messages

# Create your views here.

@login_required
def booking(request):# pass property id as a parameter
          if request.method == 'POST':
                    property_id = request.POST.get('property')
                    place = Property.objects.get(id=property_id)

                    if request.user == place.owner:
                                messages.error(request, 'You cannot book your own property')
                                return redirect(reverse('property:view', args=[property_id]))

                    if place.availabality == False:
                                messages.error(request, 'Property is not available at the moment')
                                return redirect(reverse('property:view', args=[property_id]))

                    
                    #creating a booking record
                    booking=Booking()
                    booking.user = request.user
                    booking.property = place
                    booking.start_date = request.POST.get('start_date')
                    booking.end_date = request.POST.get('end_date')
                    booking.amount = request.POST.get('amount')
                    

                    # creating transaction record
                    record=Transaction()
                    record.booking = booking
                    record.status = 3
                    

                    place.availabality= False
                    place.times_rented+=1
                    

                    renter=currentrenter.objects.create(property=place,user=booking.user)
                    #sending email
                    subject='Booking successful'
                    messages1=f'{booking.user} has successfully booked your {place.title}'
                    messages2=f'{booking.user} your booking was succesful for {place.title}'
                    send_email(subject,messages1,booking.user.email)
                    send_email(subject,messages2,place.owner.email)
                    print('mail sent succesfully')

                    
                    booking.save()
                    place.save()
                    renter.save()
                    record.save()
                    
                    

                    return render(request, 'account/profile.html')
          return render(request, 'booking/booking.html')

@login_required
def cancle(request,booking_id):
        book = Booking.objects.get(id=booking_id)
        print(book)
        print("hii")
        print(book.was_cancled)
        if book.was_cancled == False:

               #sending email
                messages2=f'{book.user} has canceled your {property.title} booking'
                messages1=f'{book.user} your booking was cancled for {property.title}'
                send_email('Booking Canceled',messages1,book.user.email)
                send_email('Booking Canceled',messages2,property.owner.email)
                print('mail sent succesfully')
                book.was_cancled = True
                print(book.was_cancled)
                book.save()

        if book.was_cancled == True:
                renter = currentrenter.objects.get(user=book.user, property=book.property)
                property=Property.objects.get(id=book.property.id)
                property.availabality = True
                property.times_rented -= 1
                property.save()
                print('heelo')
                print(renter)
                renter.delete()
        

        

            
        return redirect(reverse('account:myrental'))
    
def history(request):
    record=Booking.objects.filter(user=request.user)
    print(record)
    return render(request, 'booking/history.html', {'record': record})