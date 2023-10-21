from rest_framework import serializers
from Account.models import Users, UserStacks, Members, Pays, Professions
from django.contrib.auth.models import Permission
from Permission.serializers import RolesSerializer

class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = '__all__'

class UserStacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStacks
        fields = '__all__'

class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

class UsersSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class UsersSerializer(serializers.ModelSerializer):
    role = RolesSerializer()
    pays = PaysSerializer()
    profession = ProfessionsSerializer()
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}