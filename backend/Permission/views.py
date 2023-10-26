from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from Permission.permission_checker import PermissionChecker
from Permission.models import Roles, Permission_roles
from django.contrib.auth.models import Permission
from Permission.serializers import RolesSerializer, PermissionRolesSerializer, PermissionsSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def createRole(request):
    if not PermissionChecker.has_permission(request, 'roles_create'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    serializer = RolesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def updateRole(request, id):
    if not PermissionChecker.has_permission(request, 'roles_update'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    try:
        role = Roles.objects.get(id=id)
    except Roles.DoesNotExist:
        return Response({'message': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RolesSerializer(role, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def deleteRole(request, id):
    if not PermissionChecker.has_permission(request, 'roles_delete'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    try:
        role = Roles.objects.get(id=id)
    except Roles.DoesNotExist:
        return Response({'message': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

    role.delete()
    return Response({'message': 'Role deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def role(request, id):
    if not PermissionChecker.has_permission(request, 'roles_view'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    try:
        role = Roles.objects.get(id=id)
    except Roles.DoesNotExist:
        return Response({'message': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RolesSerializer(role)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def roles(request):
    # if not PermissionChecker.has_permission(request, 'roles_view_all'):
    #     return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    roles = Roles.objects.all()
    serializer = RolesSerializer(roles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def addPermissionToRole(request, role_id, permission_id):
    if not PermissionChecker.has_permission(request, 'add_permission_to_role'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    try:
        role = Roles.objects.get(id=role_id)
        permission = Permission.objects.get(id=permission_id)
    except Roles.DoesNotExist or Permission.DoesNotExist:
        return Response({'message': 'Role or permission not found'}, status=status.HTTP_404_NOT_FOUND)

    permission_role, created = Permission_roles.objects.get_or_create(role=role, permission=permission)
    if created:
        return Response({'message': 'Permission added to role successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'Permission already assigned to role'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def removePermissionFromRole(request, role_id, permission_id):
    if not PermissionChecker.has_permission(request, 'remove_permission_from_role'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    try:
        permission_role = Permission_roles.objects.get(role_id=role_id, permission_id=permission_id)
    except Permission_roles.DoesNotExist:
        return Response({'message': 'Permission not assigned to role'}, status=status.HTTP_404_NOT_FOUND)

    permission_role.delete()
    return Response({'message': 'Permission removed from role successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def rolePermissions(request, role_id):
    if not PermissionChecker.has_permission(request, 'view_role_permission'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    try:
        role = Roles.objects.get(id=role_id)
    except Roles.DoesNotExist:
        return Response({'message': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

    permissions = Permission_roles.objects.filter(role=role)
    serializer = PermissionsSerializer(permissions, many=True)
    return Response(serializer.data)
