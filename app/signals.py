from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_token_usuario(sender, instance, created, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)