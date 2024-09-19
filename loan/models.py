from django.db import models

class loan_reg(models.Model):
    ids = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    amount = models.IntegerField()
    ir = models.IntegerField()
    emi = models.IntegerField()
    start = models.CharField(max_length=250)
    end = models.CharField(max_length=250)
    status = models.CharField(max_length=20)


class loan_creg(models.Model):
    ids = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    amount = models.IntegerField()
    start = models.CharField(max_length=250)
    end = models.CharField(max_length=250)


class loan_check(models.Model):
    id1 = models.IntegerField()
    acc1 = models.IntegerField()
    cmob = models.IntegerField()
