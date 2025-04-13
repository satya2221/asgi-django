from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.
class Notification(models.Model):
    message = models.TextField()

    # override method save untuk broadcast via websocket
    def save(self, *args, **kwargs):
        channel = get_channel_layer() #akan tarik semua group channel yang ada

        # Proses nya async, dia gak bisa dikirimkan dalam proses sync
        # Sehingga perlu diubah dari async -> sync
        # Kita gunakan function wrapper untuk melakukan proses 
        # channel.group_send('notifications', {
        #     'type': 'send_notification', # wajib sama dengan nama method di consumer
        #     'message': self.message
        # })
        
        async_to_sync(channel.group_send)('notification', {
            'type': 'send_notification', # wajib sama dengan nama method di consumer
            'message': self.message
        })

        return super().save(**kwargs)