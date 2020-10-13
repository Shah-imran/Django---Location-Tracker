from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Device
import uuid

@receiver(post_save, sender=User)
def create_device_id(sender, instance, created, **kwargs):
    if created:
        uuid_one = uuid.uuid1()

        # create new device
        Device.objects.create(
            user=instance,
            device_id=uuid_one
        )
        print("Device id created")



@receiver(pre_save, sender=User)
def user_password(sender, instance, **kwargs):
    if instance.pk is None:
        password = instance.password
        print("User Password", password)