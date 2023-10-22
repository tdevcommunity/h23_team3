from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from BaseApi.AppEnum import *
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import BaseUserManager
from Permission.models import Roles

class Pays(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Professions(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        superUserRole, created = Roles.objects.get_or_create(name=UserRoleEnum.SUPER_ADMIN.value, defaults={'description': 'The super user'})
        extra_fields.setdefault('role_id', superUserRole.id)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    pays = models.ForeignKey('Account.Pays', on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    sexe = models.CharField(max_length=255, choices=[(sexe.value, sexe.name) for sexe in GenderEnum], null=True)
    role = models.ForeignKey('Permission.Roles', on_delete=models.CASCADE, related_name='users_role')
    profession = models.ForeignKey('Account.Professions', on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    @property
    def is_staff(self):
       return self.is_superuser

    def has_perm(self, perm, obj=None):
       return self.is_superuser

    def has_module_perms(self, app_label):
       return self.is_superuser

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value

class Stacks(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserStacks(models.Model):
    user = models.ForeignKey('Account.Users', on_delete=models.CASCADE)
    stack = models.ForeignKey(Stacks, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Members(models.Model):
    mentor = models.ForeignKey('Account.Users', related_name='mentor', on_delete=models.CASCADE)
    mentore = models.ForeignKey('Account.Users', related_name='mentore', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)