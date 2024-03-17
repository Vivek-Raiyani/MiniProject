from django.db import models

# Create your models here.
class Wishlist(models.Model):
          user = models.ForeignKey('account.User', on_delete=models.CASCADE)
          property = models.ForeignKey('property.Property', on_delete=models.CASCADE)


          def __str__(self):
                    return self.user
          
