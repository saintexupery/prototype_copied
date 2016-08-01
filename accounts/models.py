from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


UNIV_CHOICES = (
    (1, ("서울대학교")),
    (2, ("한양대학교")),
    (3, ("이화여자대학교")),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    university = models.CharField(max_length=20)

    def __str__(self):
        return self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)