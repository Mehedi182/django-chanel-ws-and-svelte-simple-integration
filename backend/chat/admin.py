from django.contrib import admin
from .models import *


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['content']


admin.site.register(Message, MessageAdmin)
