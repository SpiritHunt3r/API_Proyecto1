from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid
import datetime


def jwt_get_secret_key(user_model):
    return user_model.jwt_secret

class BusUserManager(BaseUserManager):
    def create_user(self, email, first_name , last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        user.date_joined = datetime.datetime.now()
        return user
    def create_superuser(self, email, first_name , last_name, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.date_joined = datetime.datetime.now()
        user.save(using=self._db)
        return user


    

class BusUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(default = "", max_length=255)
    last_name = models.CharField(default = "", max_length=255)
    date_joined = models.DateTimeField(default = None, null= True)
    chofer = models.ForeignKey('busdriver.BusDriver', on_delete=models.CASCADE, default = None, null = True)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
  

    objects = BusUserManager()

    REQUIRED_FIELDS = ['first_name','last_name']
    USERNAME_FIELD = 'email'
    



    def __str__(self):
        return self.email








