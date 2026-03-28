from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import List
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
@receiver(post_save,sender= List)
def notify_channels(sender,instance,created,**kwargs):
    channel_layer = get_channel_layer()
    if created:
        print("created")
        result = instance.title
        async_to_sync(channel_layer.group_send)(
        "chat_kenny",
        {
            "type": "chat.message",
            "message": result,
        }
    )
        
        pass

# @receiver(post_save, sender=Message)
# def broadcast_message(sender, instance, created, **kwargs):
#     if not created:
#         return

#     async_to_sync(channel_layer.group_send)(
#         f"chat_{instance.room_id}",
#         {
#             "type": "chat.message",
#             "id": instance.id,
#             "user": instance.user.username,
#             "content": instance.content,
#             "timestamp": instance.created_at.isoformat(),
#         }
#     )
