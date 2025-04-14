from django.db import models
from .methods import send_notification

# Create your models here.
class Notification(models.Model):
    message = models.TextField()

    def save(self, *args, **kwargs):
        send_notification(self.message)
        return super().save(**kwargs)