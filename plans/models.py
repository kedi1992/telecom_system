from django.db import models


class Plan(models.Model):
    PLAN_CHOICES = (
        ('Platinum365', 'Platinum365'),
        ('Gold180', 'Gold180'),
        ('Silver90', 'Silver90'),
    )
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.IntegerField()  # Number of days
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
