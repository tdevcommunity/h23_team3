from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny
from Permission.permission_checker import PermissionChecker
from Resource.models import Ressources, Type, Discussions
from Resource.serializers import RessourcesSerializerAdd, RessourcesSerializer, DiscussionsSerializer
from BaseApi.AppEnum import *
from django.db.models import Q
from django.db import transaction

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def addDiscussions(request, ressource_id):
    try:
        ressource = Ressources.objects.get(id=ressource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'La ressource n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)

    if not ressource.can_chat:
        return Response({'message': 'Les discussions ne sont pas autorisées pour cette ressource.'}, status=status.HTTP_403_FORBIDDEN)

    author = request.user
    content = request.data.get('content')

    discussion = Discussions(ressource=ressource, author=author, content=content)
    discussion.save()
    return Response({'message': 'Discussion ajoutée avec succès.'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def getResourceDiscussions(request, ressource_id):
    try:
        ressource = Ressources.objects.get(id=ressource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'La ressource n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)

    if not ressource.can_chat:
        return Response({'message': 'Les discussions ne sont pas autorisées pour cette ressource.'}, status=status.HTTP_403_FORBIDDEN)

    discussions = Discussions.objects.filter(ressource=ressource)
    serializer = DiscussionsSerializer(discussions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)