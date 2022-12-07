from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

GENDER = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'),)


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(
        max_length=200, choices=GENDER, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='images', default="./images/profile.webp")

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
