from django.db import models
from django.conf import settings
# Create your models here.

"""
User가 생성될 때 자동으로 Token 값을 주기 위한 방법
django의 signals와 receiver decorator를 이용한다.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
class UserComment(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
