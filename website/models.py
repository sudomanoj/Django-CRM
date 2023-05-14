from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #Automatically adds datetime of createation
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=8)
    
    def __str__(self):
        return (f'{self.first_name} {self.last_name}')
    