from django.db import models

# Create your models here.
class Property(models.Model):
          title = models.CharField(max_length=100,null=True,blank=True)
          description = models.TextField(null=True,blank=True)
          times_rented=models.IntegerField(default=0)
          availabality=models.BooleanField(default=False)

          # some property owners prefer that they rent only for particular age group, for example they prefer to rent only for students, for girls, etc
          Choices=((1,'Family'),(2,'Bachelor'),(3,'Students'),(4,'Only_for_Girls'),(5,'Only_for_Boys'),(6,'all'))
          user_preference=models.IntegerField(choices=Choices,default=6)

          owner=models.ForeignKey('account.User',on_delete=models.CASCADE)

          # write __str__ methos for all class such that deleting dont contradict

          

class propertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    default_image = models.ImageField(upload_to='media/property_images')
    image2 = models.ImageField(upload_to='media/property_images', null=True, blank=True)
    image3 = models.ImageField(upload_to='media/property_images', null=True, blank=True)
    image4 = models.ImageField(upload_to='media/property_images', null=True, blank=True)
    image5 = models.ImageField(upload_to='media/property_images', null=True, blank=True)

    

    
class propertyVideo(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    default_video = models.FileField(upload_to='media/property_videos')
    video2 = models.FileField(upload_to='media/property_videos', null=True, blank=True)

    

    
class propertyDocument(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    default_document = models.FileField(upload_to='media/property_documents')
    document2 = models.FileField(upload_to='media/property_documents', null=True, blank=True)

    



class typeOfProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    Choices=((1,'Residential'),(2,'Commercial'),(3,'Storts Ground'),(4,'Apartment'),(5,'Villa'),
             (6,'Office'),(7,'Shop'),(8,'Warehouse'),(9,'Factory'),(10,'Hotel'),
             (11,'Cottage'),(12,'Farmhouse'),(13,'Cabin'),(14,'Penthouse'),(15,'Swimming Pool'),
             (16,'Clubhouse'),(17,'Garden'),(18,'Gym'),(19,'Cinema'),(20,'Cafe'),
             (21,'Stadium'),(22,'Room')
             )
    property_type = models.IntegerField(choices=Choices,default=1)
    



    

class propertyLocation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,default='')
    state=models.CharField(max_length=100,default='')
    country=models.CharField(max_length=100,default='')
    zipcode=models.CharField(max_length=6,default='')


    
class pricing(models.Model):
    Choices=((1,'PerDay'),(2,'PerWeek'),(3,'Monthly'),(4,'Yearly'))
    property = models.ForeignKey(typeOfProperty, on_delete=models.CASCADE)
    price_type = models.IntegerField(choices=Choices,default=1)
    price = models.FloatField( default=0)




class current_renter(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)

    

