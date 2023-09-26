from django.contrib import admin
from .models import STTModel, TTSModel
# Register your models here.\

admin.site.site_header = "Speech to Text Admin"
admin.site.site_title = "Speech to Text Admin Portal"
admin.site.index_title = "Welcome to Speech to Text Researcher Portal"

admin.site.register(STTModel)
admin.site.register(TTSModel)