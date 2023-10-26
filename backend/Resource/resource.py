from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny
from Permission.permission_checker import PermissionChecker
from Resource.models import Ressources, Type, Discussions
from Resource.serializers import RessourcesSerializerAdd, RessourcesSerializer
from BaseApi.AppEnum import *

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createSession(request):
    if not PermissionChecker.has_permission(request, 'can_create_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    type = Type.objects.filter(name=TypeResourcesEnum.SESSION.value).first()

    sessionData = {
        'title': request.data.get('name'),
        'content': request.data.get('description'),
        'type_id': type.id,
        'author': request.user,
        'can_chat': False,
        'status': ResourcesStatusEnum.OPEN.value
    }
    serializer = RessourcesSerializerAdd(data=sessionData)
    if serializer.is_valid():
        session = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createMiniBlog(request):
    if not PermissionChecker.has_permission(request, 'can_create_mini_blog'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    type = Type.objects.filter(name=TypeResourcesEnum.MINI_BLOG.value).first()

    sessionData = {
        'title': request.data.get('title'),
        'content': request.data.get('content'),
        'type_id': type.id,
        'author': request.user,
        'can_chat': False,
        'status': ResourcesStatusEnum.OPEN.value
    }
    serializer = RessourcesSerializerAdd(data=sessionData)
    if serializer.is_valid():
        session = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createRequest(request):
    type = Type.objects.filter(name=TypeResourcesEnum.QUESTION.value).first()

    sessionData = {
        'title': request.data.get('question'),
        'content': request.data.get('description'),
        'type_id': type.id,
        'author': request.user,
        'can_chat': True,
        'status': ResourcesStatusEnum.OPEN.value
    }
    serializer = RessourcesSerializerAdd(data=sessionData)
    if serializer.is_valid():
        session = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)