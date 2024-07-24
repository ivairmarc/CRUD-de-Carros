from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('pre save', instance.brand)

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **Kwargs):
    print('delete', instance)