from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    avatar = models.ImageField(upload_to='user_avatars', null=True)

    def __str__(self):
        return self.user.username

