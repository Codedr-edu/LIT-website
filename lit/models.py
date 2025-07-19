from django.db import models
from froala_editor.fields import FroalaField


class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    role_order = models.PositiveIntegerField(default=0)  # Thứ tự xếp vai trò
    bio = FroalaField(blank=True)
    achievements = FroalaField(blank=True)
    contact = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='members/', blank=True)

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=200)
    content = FroalaField()
    image = models.ImageField(upload_to='stories/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    title = models.CharField(max_length=200)
    content = FroalaField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = FroalaField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    date = models.DateTimeField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
