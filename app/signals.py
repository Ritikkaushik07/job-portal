from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Datas

user=get_user_model()

@receiver(post_save, sender=user)
def create_user_profile(sender, instance, created, **kwargs):
    print("Sender -->", sender)
    print("Instance-->", instance)
    print("Created-->", created)
    if created:
        Datas.objects.create(user=instance)