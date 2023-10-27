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
from django.db.models import Q
from django.db import transaction
from Account.models import Members

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createSession(request):
    if not PermissionChecker.has_permission(request, 'can_create_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    name = request.data.get('name')
    if not name:
        return Response({'message': 'Nom requis'}, status=status.HTTP_400_BAD_REQUEST)

    type = Type.objects.filter(name=TypeResourcesEnum.SESSION.value).first()

    sessionData = {
        'title': name,
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

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def updateSession(request, resource_id):
    if not PermissionChecker.has_permission(request, 'can_update_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    try:
        session_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    if session_resource.status == ResourcesStatusEnum.CLOSED.value:
        return Response({'message': 'La session est déjà fermée'}, status=status.HTTP_400_BAD_REQUEST)

    if not PermissionChecker.has_permission(request, 'can_update_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if session_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette ressource'}, status=status.HTTP_403_FORBIDDEN)

    name = request.data.get('name')
    if not name:
        return Response({'message': 'Le nom est obligatoire'}, status=status.HTTP_400_BAD_REQUEST)

    session_resource.title = name
    session_resource.content = request.data.get('description')
    session_resource.save()

    return Response({'message': 'La ressource a été mise à jour avec succès'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def deleteSession(request, resource_id):
    if not PermissionChecker.has_permission(request, 'can_delete_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    try:
        session_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    if session_resource.status == ResourcesStatusEnum.CLOSED.value:
        return Response({'message': 'La session est déjà fermée'}, status=status.HTTP_400_BAD_REQUEST)

    if session_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette ressource'}, status=status.HTTP_403_FORBIDDEN)

    session_resource.delete()

    return Response({'message': 'Session supprimée avec succès'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getSession(request, resource_id):
    if not PermissionChecker.has_permission(request, 'can_view_session_details'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        session_resource = Ressources.objects.get(id=resource_id)
        serializer = RessourcesSerializer(session_resource)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Ressources.DoesNotExist:
        return Response({'message': 'Session non trouvée'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getMyMentorSessions(request):
    if not PermissionChecker.has_permission(request, 'can_view_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    status_filter = request.query_params.get('status')
    keyword = request.query_params.get('keyword', '')

    user = request.user
    mentors = Members.objects.filter(mentore=user, status=True).values_list('mentor', flat=True)
    
    if status_filter:
        sessions = Ressources.objects.filter(author__in=mentors, type__name=TypeResourcesEnum.SESSION.value, status=status_filter)
        sessions = sessions.order_by('-created_at')
        sessions = sessions.distinct()
    else:
        sessions = Ressources.objects.filter(author__in=mentors, type__name=TypeResourcesEnum.SESSION.value)
        sessions = sessions.order_by('-created_at')
        sessions = sessions.distinct()

    if keyword:
        sessions = sessions.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    serializer = RessourcesSerializer(sessions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getMySessions(request):
    if not PermissionChecker.has_permission(request, 'can_view_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    status_filter = request.query_params.get('status')
    keyword = request.query_params.get('keyword', '')

    user = request.user
        
    if status_filter:
        sessions = Ressources.objects.filter(author=user, type__name=TypeResourcesEnum.SESSION.value, status=status_filter)
        sessions = sessions.order_by('-created_at')
        sessions = sessions.distinct()
    else:
        sessions = Ressources.objects.filter(author=user, type__name=TypeResourcesEnum.SESSION.value)
        sessions = sessions.order_by('-created_at')
        sessions = sessions.distinct()

    if keyword:
        sessions = sessions.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    serializer = RessourcesSerializer(sessions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getSessions(request):
    if not PermissionChecker.has_permission(request, 'can_view_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    status_filter = request.query_params.get('status')
    keyword = request.query_params.get('keyword', '')

    user = request.user

    if status_filter:
        sessions = Ressources.objects.filter(type__name=TypeResourcesEnum.SESSION.value, status=status_filter)
        sessions = sessions.order_by('-created_at')
        sessions = sessions.distinct()
    else:
        sessions = Ressources.objects.filter(type__name=TypeResourcesEnum.SESSION.value)
        sessions = sessions.order_by('-created_at')
        sessions = sessions.distinct()

    if keyword:
        sessions = sessions.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    serializer = RessourcesSerializer(sessions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def closeOrOpenSession(request, resource_id):
    if not PermissionChecker.has_permission(request, 'can_close_or_open_session'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    try:
        session_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)
    
    if session_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette ressource'}, status=status.HTTP_403_FORBIDDEN)
    
    if session_resource.status == ResourcesStatusEnum.CLOSED.value:
        session_resource.status = ResourcesStatusEnum.OPEN.value
        message = 'Session ouverte'
    else:
        session_resource.status = ResourcesStatusEnum.CLOSED.value
        message = 'Session fermée'
    
    session_resource.save()
    return Response({'message': f'{message} avec succès'}, status=status.HTTP_200_OK)