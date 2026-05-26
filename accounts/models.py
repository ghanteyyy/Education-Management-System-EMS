from django.db import models
from django.db.models import Q
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from utils import utils


class CustomUserManager(BaseUserManager):
    '''
    Define a model manager for User model with no username field
    '''

    def _create_user(self, email, password=None, **extra_fields):
        '''
        Create and save a User with the given email and password
        '''

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        '''
        Create and save a SuperUser with the given email and password
        '''

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserRole(models.TextChoices):
    ORGANIZATION = "organization", "Organization"
    STUDENT = "student", "Student"
    STAFF = "staff", "Staff"


class CustomUser(AbstractUser):
    '''
    Custom user model representing an individual user.
    '''

    username = None
    id = models.CharField(primary_key=True, editable=False, default=utils.generate_ids, max_length=255)
    email = models.EmailField(
                verbose_name=_('email address'),
                unique=True,
                error_messages={
                    "unique": _("A user with this email already exists."),
                }
            )

    role = models.CharField(max_length=20, choices=UserRole.choices)


    # --- Auth Settings ---
    USERNAME_FIELD = 'email'  # Use email for auth
    REQUIRED_FIELDS = []  # No additional required fields

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
