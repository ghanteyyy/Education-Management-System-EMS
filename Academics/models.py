from django.db import models
from Organizations.models import Organization, Academic_Year
from Employees.models import Teacher
from utils import utils


class Class(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=utils.generate_ids)
    academic_year = models.ForeignKey(Academic_Year, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    section = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=utils.generate_ids)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(Academic_Year, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
