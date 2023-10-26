from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework.permissions import AllowAny
from Permission.permission_checker import PermissionChecker
from Account.models import Pays, Professions, Stacks
from Account.serializers import PaysSerializer, ProfessionsSerializer, StacksSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def countries(request):
    countries = Pays.objects.all()
    serializer = PaysSerializer(countries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def professions(request):
    professions = Professions.objects.all()
    serializer = ProfessionsSerializer(professions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def stacks(request):
    stacks = Stacks.objects.all()
    serializer = StacksSerializer(stacks, many=True)
    return Response(serializer.data)