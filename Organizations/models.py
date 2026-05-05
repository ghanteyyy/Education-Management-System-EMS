from utils import utils
from django.db import models
from django.contrib.auth.hashers import make_password


class Organization(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)

    name = models.CharField(max_length=255)
    abbr = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Academic_Year(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='academic_years')

    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Document(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='documents')

    file_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notice(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='notices')

    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='events')

    title = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Event_Image(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='notices')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')

    image_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
