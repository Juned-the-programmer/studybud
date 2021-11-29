from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="static/profiles")
    bio = models.TextField()

    def __str__(self):
        return self.user.username

def create_profile(sender,instance,created,**Kwargs):
    if created:
        profile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)
