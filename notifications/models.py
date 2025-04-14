from django.db import models
from .tasks import task_send_notification

# Create your models here.
class Notification(models.Model):
    message = models.TextField()

    def save(self, *args, **kwargs):
        task_send_notification(self.message)
        return super().save(**kwargs)