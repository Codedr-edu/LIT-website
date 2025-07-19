from django.contrib import admin
from .models import News, Event, Story, Member, ContactMessage
# Register your models here.
admin.site.register(News)
admin.site.register(Event)
admin.site.register(Story)
admin.site.register(Member)
admin.site.register(ContactMessage)
