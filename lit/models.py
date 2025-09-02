from django.db import models
from tinymce import models as tinymce_models
# from froala_editor.fields import models.TextField


class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    role_order = models.PositiveIntegerField(default=0)  # Thứ tự xếp vai trò
    bio = tinymce_models.HTMLField()
    achievements = tinymce_models.HTMLField()
    contact = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='members/', blank=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='stories/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    address = models.TextField(blank=True, null=True)
    organizer = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    registration_link = models.URLField(blank=True, null=True)
    date = models.DateTimeField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = tinymce_models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
