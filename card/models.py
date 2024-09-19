from django.db import models

class card_db(models.Model):
    card_id = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=20)
    card_type = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)  # Assuming card number is stored as a string
    expiry_date = models.CharField(max_length=20)   # Format MM/YY
    cvv = models.CharField(max_length=4)           # CVV length may vary, but 3-4 is common
    status = models.CharField(max_length=10)
# Create your models here.



