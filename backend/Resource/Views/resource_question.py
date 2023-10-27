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
def createRequest(request):
    question = request.data.get('question')
    description = request.data.get('description')
    if not question or not description:
        return Response({'message': 'La question et la description sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST)

    type = Type.objects.filter(name=TypeResourcesEnum.QUESTION.value).first()

    sessionData = {
        'title': question,
        'content': description,
        'type_id': type.id,
        'author': request.user,
        'can_chat': True,
        'status': ResourcesStatusEnum.OPEN.value
    }
    serializer = RessourcesSerializerAdd(data=sessionData)
    if serializer.isvalid():
        session = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def updateRequest(request, resource_id):
    try:
        request_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    if request_resource.status == ResourcesStatusEnum.CLOSED.value:
        return Response({'message': 'La ressource est déjà fermée'}, status=status.HTTP_400_BAD_REQUEST)

    if request_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette ressource'}, status=status.HTTP_403_FORBIDDEN)

    question = request.data.get('question')
    description = request.data.get('description')
    if not question or not description:
        return Response({'message': 'La question et la description sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST)

    request_resource.title = question
    request_resource.content = description
    request_resource.save()

    return Response({'message': 'La ressource a été mise à jour avec succès'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def deleteRequest(request, resource_id):
    try:
        request_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    if request_resource.status == ResourcesStatusEnum.CLOSED.value:
        return Response({'message': 'La ressource est déjà fermée'}, status=status.HTTP_400_BAD_REQUEST)

    if request_resource.author != request.user:
        return Response({'message': 'Vous n\'êtes pas l\'auteur de cette question'}, status=status.HTTP_403_FORBIDDEN)

    request_resource.delete()

    return Response({'message': 'Question suppimée avec succès'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def getRequest(request, resource_id):
    try:
        request_resource = Ressources.objects.get(id=resource_id)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    try:
        request_resource = Ressources.objects.get(id=resource_id)
        serializer = RessourcesSerializer(request_resource)
        return Response(serializer.data)
    except Ressources.DoesNotExist:
        return Response({'message': 'Question non trouvée'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def getRequests(request):
    status_filter = request.query_params.get('status')
    stack_names = request.query_params.get('stack_names', '')
    keyword = request.query_params.get('keyword', '')

    if status_filter:
        requests = Ressources.objects.filter(type__name=TypeResourcesEnum.QUESTION.value, status=status_filter)
    else:
        requests = Ressources.objects.filter(type__name=TypeResourcesEnum.QUESTION.value)

    if stack_names:
        stack_names_list = [name.strip() for name in stack_names.split(',')]
        requests = requests.filter(stacks__name__in=stack_names_list)

    if keyword:
        requests = requests.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword))

    serializer = RessourcesSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def closeOrOpenRequest(request, resource_id):
    try:
        request_resource = Ressources.objects.get(id=resource_id)
        if request_resource.author != request.user:
            return Response({'message': 'Vous n\'êtes pas l\'auteur de cette question'}, status=status.HTTP_403_FORBIDDEN)

        if request_resource.status == ResourcesStatusEnum.CLOSED.value:
            request_resource.status = ResourcesStatusEnum.OPEN.value
            message = 'La question a été ouverte'
        else:
            request_resource.status = ResourcesStatusEnum.CLOSED.value
            message = 'La question a été fermée'
        request_resource.save()
        return Response({'message': f'{message} avec succès'}, status=status.HTTP_200_OK)
    except Ressources.DoesNotExist:
        return Response({'message': 'Ressource non trouvée'}, status=status.HTTP_404_NOT_FOUND)
