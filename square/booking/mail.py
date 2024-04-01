from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message,receiver):
          from_email = settings.EMAIL_HOST_USER
          recipient_list = [receiver]
          send_mail(subject, message, from_email, recipient_list, fail_silently=False)
          print('mail func called')
