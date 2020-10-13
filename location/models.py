from django.db import models
import datetime
from django.contrib.auth.models import User


class Device(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Active")
    device_id = models.CharField(max_length=200)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.device_id}"

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_time = models.DateTimeField(default=datetime.datetime.utcnow)

    uploaded_by = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.latitude)} - {str(self.longitude)}"
