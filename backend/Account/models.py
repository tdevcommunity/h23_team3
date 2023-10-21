from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from BaseApi.AppEnum import GenderEnum

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

class Users(AbstractBaseUser):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    pays = models.ForeignKey('Account.Pays', on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    sexe = models.CharField(max_length=255, choices=[(sexe.value, sexe.name) for sexe in GenderEnum], null=True)
    role = models.ForeignKey('Permission.Roles', on_delete=models.CASCADE, related_name='users_role')
    profession = models.ForeignKey('Account.Professions', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'

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