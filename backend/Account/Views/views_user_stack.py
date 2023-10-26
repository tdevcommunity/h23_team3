from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework.permissions import AllowAny
from Permission.permission_checker import PermissionChecker
from django.shortcuts import get_object_or_404
from Account.models import Stacks, Users, UserStacks
from Account.serializers import UserStacksSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createUserStack(request):
    if not PermissionChecker.has_permission(request, 'add_userstacks'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    user = request.user
    stack_ids = request.data.get('stacks', [])
    stacks = Stacks.objects.filter(id__in=stack_ids)

    if stacks.count() != len(stack_ids):
        return Response({'message': 'Certains stacks n\'ont pas été trouvés'}, status=status.HTTP_404_NOT_FOUND)

    existing_userstacks = UserStacks.objects.filter(user=user, stack__in=stacks)
    existing_stack_ids = set(existing_userstacks.values_list('stack', flat=True))
    stacks_to_create = [stack for stack in stacks if stack.id not in existing_stack_ids]

    userstacks_list = [UserStacks(user=user, stack=stack) for stack in stacks_to_create]
    batch_size = len(userstacks_list)
    if batch_size <= 0:
        return Response({'message': 'Aucun stacks ajouter'}, status=status.HTTP_400_BAD_REQUEST) 
    UserStacks.objects.bulk_create(userstacks_list, batch_size=batch_size)

    return Response({'message': 'UserStacks créés avec succès'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def deleteUserStacks(request):
    if not PermissionChecker.has_permission(request, 'delete_userstacks'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    user_id = request.data.get('user')
    stack_id = request.data.get('stack')

    user = get_object_or_404(Users, id=user_id)
    stack = get_object_or_404(Stacks, id=stack_id)
    try:
        user_stack = UserStacks.objects.get(user=user, stack=stack)
    except UserStacks.DoesNotExist:
        return Response({'message': 'La relation UserStacks n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    user_stack.delete()

    return Response({'message': 'UserStacks supprimé avec succès'}, status=status.HTTP_200_OK)
