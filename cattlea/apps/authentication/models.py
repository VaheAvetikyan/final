from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import validate_email


# Defining Custom user manager which extends Django BaseUserManager model
class CustomUserManager(BaseUserManager):

    def create_user(self, email=None, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError("To register you should provide an email")
        if validate_email(email):
            raise ValueError("Invalid email")
        if not first_name or first_name == " ":
            raise ValueError("To register you should provide your first name")
        if not last_name or last_name == " ":
            raise ValueError("To register you should provide your last name")
        if not password or len(password) < 8:
            raise ValueError("Your password must be at least 8 characters")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, first_name=None, last_name=None, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Defining Custom user model which extends Django default AbstractBaseUser model
class User(AbstractBaseUser):

    email = models.EmailField('email address', unique=True, blank=False)
    first_name = models.CharField('first name', max_length=30, null=False)
    last_name = models.CharField('last name', max_length=30, blank=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    address = models.ForeignKey(
        'Address', related_name='address', on_delete=models.SET_NULL, blank=True, null=True
        )

    """Set username_field to email, so that users login with their emails"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Specifying the manager for this model
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True



class Address(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=64)
    
    street_address = models.CharField(max_length=64)
    apartment_address = models.CharField(max_length=64, null=True)
    
    zip = models.CharField(max_length=16)

    '''
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    '''

    default = models.BooleanField(default=False)

    def __str__(self):
        return self.street_address

    class Meta:
        verbose_name_plural = 'Addresses'
