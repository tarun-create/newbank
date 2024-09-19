from django.db import models

# Create your models here.
class user_register(models.Model):
    user_name = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=120)
    role = models.CharField(max_length=20)
    


class Createaccount(models.Model):

    user_name = models.CharField(max_length=50)  
    mobile_no = models.IntegerField() 
    email = models .CharField(max_length=50)
    utype = models .CharField(max_length=10)
    message = models.CharField(max_length=100)
    balance = models.CharField(max_length=100,blank=True,default=0.00)

class Createaccountuser(models.Model):
    user_name = models.CharField(max_length=50)  
    mobile_no = models.IntegerField() 
    email = models .CharField(max_length=50)
    utype = models .CharField(max_length=10)
    message = models.CharField(max_length=100)


class create_nominee(models.Model):
    name = models.CharField(max_length=50)  
    mobile_no = models.IntegerField() 
    relationship = models .CharField(max_length=50)
    date = models .DateField(max_length=10)
    address = models.CharField(max_length=100) 

class create_reference(models.Model):
    name = models.CharField(max_length=50)  
    mobile_no = models.IntegerField() 
    address1 = models.CharField(max_length=10)
    message = models.CharField(max_length=100)   

class create_documents(models.Model):
    photo = models.FileField()  
    aadhar_card = models.FileField() 
    pan_card = models .FileField()  

    
class UserLogin(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=120)


class PaymentDetailsTable(models.Model):
  cardtype = models.CharField(max_length=255)
  cardholdername=models.CharField(max_length=255)
  cardnumber=models.CharField(max_length=16)
  expirydate=models.CharField(max_length=255)
  cvv=models.CharField(max_length=3)

class accountpayTable(models.Model):
    account_Name = models.CharField(max_length=255)
    account_Number=models.CharField(max_length=255)
    ifsc=models.CharField(max_length=16)
    amount=models.CharField(max_length=255)

class payeedetailsTable(models.Model):
    account_Name = models.CharField(max_length=255)
    account_Number=models.CharField(max_length=255)
    ifsc=models.CharField(max_length=16)
    bankname=models.CharField(max_length=255)


