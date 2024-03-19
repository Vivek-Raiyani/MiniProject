from django.shortcuts import render   
from .models import Booking, Transaction, cancalation 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def booking(request, property_id):
          if request.method == 'POST':
                    #creating a booking record
                    booking=Booking()
                    booking.user = request.user

                    booking.property = property.objects.get(id=property_id)
                    booking.start_date = request.POST.get('start_date')
                    booking.end_date = request.POST.get('end_date')
                    booking.amount = request.POST.get('amount')
                    booking.save()

                    # creating transaction record
                    record=Transaction()
                    record.booking = booking
                    record.status = 3
                    record.save()

                    return render(request, 'account/profile.html')
          return render(request, 'booking/booking.html')

@login_required
def cancle(request,transaction_id):
    if request.method== "POST":
        transaction = Transaction.objects.get(id=transaction_id)
        cancle=cancalation()
        if transaction.status == 1:
               cancle.user = request.user
               cancle.reason = request.POST.get('reason')
               cancle.transaction = transaction
               cancle.charges = transaction.amount * 0.1
               cancle.refund_amount = transaction.amount - cancle.charges
               cancle.save()
               transaction.status = 4
               transaction.save()
               transaction.booking.was_cancled = True
               transaction.booking.save()
               transaction.booking.property.availabality = True
               transaction.booking.property.save()
        return render(request, 'account/profile.html')