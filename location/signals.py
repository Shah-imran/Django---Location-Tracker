from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Device, Account
import uuid

@receiver(post_save, sender=Account)
def create_user_device(sender, instance, created, **kwargs):

    if created:

        print("Your password is", instance.password)

        # create a user
        user = User.objects.create_user(
            username=instance.username,
            email=instance.email,
            password=instance.password
        )

        email_body = f"""
            Your account has been created.
            Username : {user.username}
            Email : {user.email}
            Password : {instance.password}
        """

        user.email_user("User account created", email_body)

        uuid_one = uuid.uuid1()

        # create new device
        # Device.objects.create(
        #     user=user,
        #     device_id=uuid_one
        # )
        # print("Device id created")
