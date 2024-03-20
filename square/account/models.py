from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.utils import timezone

# Create your models here.
class CustomUserManager(UserManager):
        def _create_user(self,email,password,**extra_fields):
                if not email:
                        raise ValueError('The given email must be set')
                email = self.normalize_email(email)
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        
        def create_user(self, email=None,password=None, **extra_fields):
                extra_fields.setdefault('is_staff', False)
                extra_fields.setdefault('is_superuser', False)
                return self._create_user(email, password, **extra_fields)

        def create_superuser(self, email=None, password=None, **extra_fields):
                extra_fields.setdefault('is_staff', True)
                extra_fields.setdefault('is_superuser', True)

                if extra_fields.get('is_staff') is not True:
                        raise ValueError('Superuser must have is_staff=True.')
                if extra_fields.get('is_superuser') is not True:
                        raise ValueError('Superuser must have is_superuser=True.')

                return self._create_user(email, password, **extra_fields)
        
'''
In Django, you don't necessarily need to create a custom manager to use email for authentication.
 Django's built-in authentication system already supports using email as the unique identifier for authentication without requiring a custom manager.
'''
         
class User(AbstractUser):
          email=models.EmailField(unique=True,default='')
          name=models.CharField(max_length=50, default='')
          phone_no=models.CharField(max_length=10, default='',null=True,blank=True)
          profile_pic=models.ImageField(upload_to='media/profile_pic', null=True,blank=True)

          # option of to select gender of the user
          Choices=((1,'Male'),(2,'Female'),(3,'Others'))
          gender=models.IntegerField(choices=Choices,default=1)
          # options to select from for type of user is our service partner or service user
          Choices_type=((1,'Service_User'),(2,'Service_Partner'))
          user_type=models.IntegerField(choices=Choices_type,default=1)

          is_active=models.BooleanField(default=True)
          is_staff=models.BooleanField(default=False)
          is_superuser=models.BooleanField(default=False)

          date_joined=models.DateTimeField(default=timezone.now)
          last_login=models.DateTimeField(null=True,blank=True)

          objects=CustomUserManager()# points to user manager we have created

          USERNAME_FIELD='email'  # authention using email
          EMAIL_FIELD='email' #specify the field used for email identification
          REQUIRED_FIELDS = ['username','phone_no','gender','user_type']  # additional required fields for user creation
                    

          class Meta:
                    verbose_name = 'User'
                    verbose_name_plural = 'Users'
