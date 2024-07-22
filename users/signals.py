from django.db.models.signals import post_save
#if when .save() method work in the register view it will send a signal 
from django.contrib.auth.models import User
from django.dispatch import receiver #this will receive the signal and create profile for the user 
from .models import Profile

@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs): #instance is the user that is registered , created: returns true if the user is created, 
    if created:
        Profile.objects.create(user=instance)