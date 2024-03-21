from django.db import models

# Create your models here.
class Booking(models.Model):
          user = models.ForeignKey('account.User', on_delete=models.CASCADE)
          property = models.ForeignKey('property.Property', on_delete=models.CASCADE)
          start_date = models.DateField()
          end_date = models.DateField()
          amount=models.IntegerField(default=0)
          was_cancled=models.BooleanField(default=False)

          def __str__(self):
            return f'{self.user} - {self.property}'

class Transaction(models.Model):
          Choices=((1,'Succes'),(2,'Failure'),(3,'Pending'),(4,'Cancled'))
          status=models.IntegerField(choices=Choices,default=3)
          booking= models.OneToOneField('booking.Booking', on_delete=models.CASCADE)

          def __str__(self):
            return f'{self.booking} - {self.status}'

class cancalation(models.Model):
          user = models.ForeignKey('account.User', on_delete=models.CASCADE)
          reason = models.TextField( null=True, blank=True)
          transaction = models.OneToOneField('booking.Transaction', on_delete=models.CASCADE, null=True)
          charges = models.FloatField(default=0)
          refund_amount = models.FloatField(default=0)
          def __str__(self):
            return f'{self.user} - {self.transaction}'