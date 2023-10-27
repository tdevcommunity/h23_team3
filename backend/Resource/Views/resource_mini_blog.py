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

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createMiniBlog(request):
    if not PermissionChecker.has_permission(request, 'can_create_mini_blog'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    title = request.data.get('title')
    content = request.data.get('content')
    if not title or not content:
        return Response({'message': 'Le titre et le contenu sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST)
    
    type = Type.objects.filter(name=TypeResourcesEnum.MINI_BLOG.value).first()

    sessionData = {
        'title': title,
        'content': content,
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
def updateMiniBlog(request, resource_id):
    if not PermissionChecker.has_permission(request, 'can_update_mini_blog'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    try:
        miniblog_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    if miniblog_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette ressource'}, status=status.HTTP_403_FORBIDDEN)

    title = request.data.get('title')
    content = request.data.get('content')
    if not title or not content:
        return Response({'message': 'Le titre et le contenu sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST)

    miniblog_resource.title = title
    miniblog_resource.content = content
    miniblog_resource.save()

    return Response({'message': 'La ressource a été mise à jour avec succès'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def deleteMiniBlog(request, resource_id):
    if not PermissionChecker.has_permission(request, 'can_delete_mini_blog'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    try:
        miniblog_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    if miniblog_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette ressource'}, status=status.HTTP_403_FORBIDDEN)

    miniblog_resource.delete()

    return Response({'message': 'Mini blog supprimé avec succès.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def getMiniBlog(request, resource_id):
    try:
        miniblog_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RessourcesSerializer(miniblog_resource)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getMiniBlogs(request):
    keyword = request.GET.get('keyword', '') 
    author_id = request.GET.get('author_id', None) 
    stack_names = request.GET.get('stack_names', '')

    miniblogs = Ressources.objects.filter(type__name=TypeResourcesEnum.MINI_BLOG.value)

    if keyword:
        miniblogs = miniblogs.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))
    if author_id is not None:
        miniblogs = miniblogs.filter(author_id=author_id)
    if stack_names:
        stack_names_list = [name.strip() for name in stack_names.split(',')]
        miniblogs = miniblogs.filter(stacks__name__in=stack_names_list)

    miniblogs = miniblogs.order_by('-created_at')

    serializer = RessourcesSerializer(miniblogs, many=True)
    return Response(serializer.data)