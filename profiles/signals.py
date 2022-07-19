''' Imports for signals setup '''
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    ''' Once a user is saved, create a profile object where the user
        is equal to the instance of the user created. If the user already
        exists but has no profile then create one for them.
    '''
    if created:
        Profile.objects.create(user=instance)
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    ''' Once profile has been created, save it '''
    instance.profile.save()