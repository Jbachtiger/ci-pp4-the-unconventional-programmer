''' Profile Model Imports '''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField


# Profile Model
class Profile(models.Model):
    ''' Profile Model '''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    profile_image = CloudinaryField('image', blank=True)
    bio = models.TextField()

    def __str__(self):
        """ To return the user's username object as a string """
        return f'Profile for {self.user.username}'


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
