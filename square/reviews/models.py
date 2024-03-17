from django.db import models

# Create your models here.
class reviews(models.Model):
    
    property = models.ForeignKey('property.Property', on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    review = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.property.title
    
class rating(models.Model):
    property = models.ForeignKey('property.Property', on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    Choices=((1,1),(2,2),(3,3),(4,4),(5,5))
    rating = models.IntegerField(choices=Choices,null=True,blank=True)

    def __str__(self):
        return f'{self.property.title}-{self.rating}'