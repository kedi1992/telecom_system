from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Renewal
from datetime import date


@receiver(post_save, sender=Customer)
def create_initial_renewal(sender, instance, created, **kwargs):
    """
    Signal receiver to create initial renewal when a new customer is created.
    """
    if created:
        renewal = Renewal(customer=instance, renewal_date=date.today(), plan_status='Active')
        renewal.save()
