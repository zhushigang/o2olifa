# from django.db import models

# # Create your models here.
from django.db import models

class Order(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=2,
                                      choices=GENDER_CHOICES,
                                      default=MALE)
    mobile_number = models.CharField(max_length=10, default='')
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='')
    date = models.DateField('time of date', null=True);
    time = models.TimeField('time of service', null=True)

class ServiceSlot(models.Model):
    date = models.DateField('service date', null=True)
    time = models.DateTimeField('service start time', null=True)
    available = models.BooleanField()

# from django.db import models

# # Create your models here.

# class Order(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     GENDER_CHOICES = (
#         (MALE, 'MALE'),
#         (FEMALE, 'FEMALE'),
#     )
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     gender = models.CharField(max_length=2,
#                                       choices=GENDER_CHOICES,
#                                       default=MALE)
#     time = models.DateTimeField('time of service')

# class ServiceSlot(models.Model):
#     time = models.DateTimeField('service start time')
#     available = models.BooleanField()