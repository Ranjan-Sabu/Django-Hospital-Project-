from typing import Any
from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()

    def __str__(self):
        return self.dep_name
    
class Doctors(models.Model):
    doctr_name = models.CharField(max_length=100)
    doctr_speci = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doctr_image = models.ImageField(upload_to='doctors')
    
    def __str__(self):
        return 'Dr.' + self.doctr_name + '-('+ self.doctr_speci +')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doctr_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date =models.DateField()
    booked_on =models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name

