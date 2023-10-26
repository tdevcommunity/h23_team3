from django.db import models
from BaseApi.AppEnum import ResourcesStatusEnum

class Type(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ressources(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    type = models.ForeignKey('Resource.Type', on_delete=models.CASCADE)
    author = models.ForeignKey('Account.Users', on_delete=models.CASCADE)
    can_chat = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=[(ResourceStatus.value, ResourceStatus.name) for ResourceStatus in ResourcesStatusEnum])
    stacks = models.ManyToManyField('Account.Stacks', related_name='resource_stacks_associate')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Discussions(models.Model):
    ressource = models.ForeignKey('Resource.Ressources', on_delete=models.CASCADE)
    author = models.ForeignKey('Account.Users', on_delete=models.CASCADE)
    content = models.TextField()