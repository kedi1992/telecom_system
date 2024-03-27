from django.db import models
from plans.models import Plan


class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    aadhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField()
    assigned_mobile_number = models.CharField(max_length=10, unique=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Renewal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    renewal_date = models.DateField()
    plan_status = models.CharField(max_length=20)

    def __str__(self):
        return f"Renewal for {self.customer.name} on {self.renewal_date}"
