import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils import timezone


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class PlannerNote(models.Model):
    """Database model for the planner notes"""
    notes_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Returns string representation of the planner notes"""
        return self.notes_text

    def was_published_recently(self):
        """Returns the publication date of the planner notes"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Diary(models.Model):
    """Database model for the diary entries"""
    diary_entry = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Returns string representation of the diary entry"""
        return self.diary_entry

    def was_published_recently(self):
        """Returns the publication date of the diary entry"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    