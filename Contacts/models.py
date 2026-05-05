from django.db import models
from Organizations.models import Organization
from utils import utils


class Province(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)

    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)

    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="districts")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)

    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="municipalities")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='contacts')
    owner_id = models.CharField(max_length=64)

    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    ward_number = models.CharField(max_length=10)
    tole = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
