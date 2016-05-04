# from django.db import models

# # Create your models here.

# class Order(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     GENDER_CHOICES = (
#         (MALE, 'MALE'),
#         (FEMALE, 'FEMALE'),
#     )
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     gender = models.CharField(max_length=2,
#                                       choices=GENDER_CHOICES,
#                                       default=MALE)
#     mobile_number = models.CharField(max_length=10)
#     address1 = models.CharField(max_length=200)
#     address2 = models.CharField(max_length=200)
#     date = models.DateField('time of date');
#     time = models.TimeField('time of service')

# class ServiceSlot(models.Model):
#     date = models.DateField('service date')
#     time = models.DateTimeField('service start time')
#     available = models.BooleanField()

from django.db import models

# Create your models here.

class Order(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=2,
                                      choices=GENDER_CHOICES,
                                      default=MALE)
    time = models.DateTimeField('time of service')

class ServiceSlot(models.Model):
    time = models.DateTimeField('service start time')
    available = models.BooleanField()