''' Profile Model Imports '''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Profile Model
class Profile(models.Model):
    ''' Profile Model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_image = CloudinaryField('image', blank=True)
    bio = models.TextField()

    def __str__(self):
        """ To return the user's username object as a string """
        return f'Profile for {self.user.username}'
