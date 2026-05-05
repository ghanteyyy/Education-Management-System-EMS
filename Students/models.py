from django.db import models
from django.contrib.auth.hashers import make_password
from Organizations.models import Organization, Academic_Year
from Employees.models import Gender_Type
from Contacts.models import Contact
from utils import utils


class Relationship_Type(models.TextChoices):
    FATHER = 'FATHER', 'Father'
    MOTHER = 'MOTHER', 'Mother'
    GUARDIAN = 'GUARDIAN', 'Guardian'
    SIBLING = 'SIBLING', 'Sibling'
    STEP_PARENT = 'STEP_PARENT', 'Step Parent'


class Student(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(Academic_Year, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    dob = models.DateField()
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=Gender_Type.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Parent(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids, editable=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=20, choices=Relationship_Type.choices)

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Previous_Organization(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    passed_year = models.CharField(max_length=4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
