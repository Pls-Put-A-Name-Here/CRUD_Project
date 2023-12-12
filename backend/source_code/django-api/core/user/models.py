from typing import Any
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db import models

# User Model and User Manager
#22-02-05

class UserManager(BaseUserManager):
    def get_object_by_public_id(self,public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist,ValueError,TypeError):
            raise Http404
        
    def create_user(self,username,email,password=None, **extra_fields):
        """Create and return a `User` with an email,bio, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')
        if password is None:
            raise TypeError('Users must have a password.')
        user = self.model(username=username,email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None, **extra_fields):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password.')
        if username is None:
            raise TypeError('Superusers must have a username.')
        if email is None:
            raise TypeError('Superusers must have an email address.')
        user = self.create(username,email,password=password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User (AbstractBaseUser,PermissionsMixin):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True,db_index=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    def __str__(self) -> str:
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    
