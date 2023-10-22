from rest_framework import serializers
from Account.models import Users, UserStacks, Members, Pays, Professions
from django.contrib.auth.models import Permission
from Resource.models import Ressources, Discussions, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class RessourcesSerializerAdd(serializers.ModelSerializer):
    class Meta:
        model = Ressources
        fields = '__all__'

class RessourcesSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    author = UsersSerializer()
    class Meta:
        model = Ressources
        fields = '__all__'

class DiscussionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussions
        fields = '__all__'