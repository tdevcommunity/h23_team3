from rest_framework import serializers
from Permission.models import Roles, Permission_roles
from django.contrib.auth.models import Permission

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class PermissionRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission_roles
        fields = '__all__'