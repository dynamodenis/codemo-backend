from django.db.models.signals import post_save
from django.conf import settings
from .models import Profile
from django.dispatch import receiver

from django.contrib.auth import get_user_model

User=get_user_model()

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile(sender,instance,created,**kwargs):
    if created:
        print('created by instance')
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()