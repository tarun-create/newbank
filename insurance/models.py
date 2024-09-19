from django.db import models

# Create your models here.
from django.db import models

class HealthInsuranceApplication(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    medical_history = models.TextField()
    health_doc = models.FileField(upload_to='health_docs/')
    

class   LifeInsuranceApplication(models.Model):
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    policy_amount = models.DecimalField(max_digits=10, decimal_places=2)
    identity_doc = models.FileField(upload_to='life_insurance_documents/')

   
class VehicleInsuranceApplication(models.Model):
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    insurance_doc = models.FileField(upload_to='insurance_documents/')

