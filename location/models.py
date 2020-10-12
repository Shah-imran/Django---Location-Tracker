from django.db import models
import datetime
from django.contrib.auth.models import User

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_time = models.DateTimeField(default=datetime.datetime.utcnow)

    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.latitude)} - {str(self.longitude)}"