from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from Organizations.models import Organization
from utils import utils


class Employee_Type(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    TEACHER = 'TEACHER', 'Teacher'
    STAFF = 'STAFF', 'Staff'


class Gender_Type(models.TextChoices):
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female'
    OTHERS = 'OTHERS', 'Others'


class Employee(models.Model):
    id = models.CharField(max_length=64, primary_key=True, default=utils.generate_ids, editable=False)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='employees')

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=Gender_Type.choices)
    employee_type = models.CharField(max_length=20, choices=Employee_Type.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="teacher_profile")

    def clean(self):
        if self.employee.employee_type != Employee_Type.TEACHER:
            raise ValidationError("Employee must be of type TEACHER")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.employee.name
