from django.db import models

# Create your models here.
class Booking(models.Model):
          user = models.ForeignKey('account.User', on_delete=models.CASCADE)
          property = models.ForeignKey('property.Property', on_delete=models.CASCADE)
          start_date = models.DateField()
          end_date = models.DateField()
          amount=models.IntegerField(default=0)

          def __str__(self):
            return f'{self.user.username} - {self.property.title}'

class Transaction(models.Model):
          Choices=((1,'Succes'),(2,'Failure'),(3,'Pending'))
          status=models.IntegerField(choices=Choices,default=3)
          booking= models.ForeignKey('booking.Booking', on_delete=models.CASCADE)

          def __str__(self):
            return f'{self.booking.Property.title} - {self.status}'
