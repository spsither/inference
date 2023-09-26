from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class STTModel(models.Model):
    audio = models.FileField(upload_to="stt", default=None, null=False, blank=False)
    text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.audio.name}:{self.text}"


class TTSModel(models.Model):
    text = models.TextField(default=None, blank=False, null=False)
    audio = models.FileField(upload_to="tts", default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey("auth.User", on_delete=models.RESTRICT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.text}:{self.audio.name}"
