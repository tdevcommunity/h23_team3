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
from Permission.models import Roles
from BaseApi.AppEnum import *
from Account.models import Users, Members
from Account.serializers import UsersSerializerAdd, UsersSerializer, MembersSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
@transaction.atomic
def register(request):
    """
    Register a new user.
    """
    # Check if the request has the required fields
    if not ('username' in request.data and 'email' in request.data and 'password' in request.data and 'role_id' in request.data):
        return Response({
           'message': 'Please provide username, email, role_id, country and password.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    statusAccount = True
    role_id = request.data['role_id']
    role = get_object_or_404(Roles, id=role_id)
    if role.name == UserRoleEnum.MENTOR.value:
        statusAccount = False

    new_user = {
        'username': request.data.get('username'),
        'email': request.data.get('email'),
        'password': make_password(request.data.get('password')),
        'role': role_id,
        'pays': request.data.get('country'),
        'sexe':  request.data.get('sexe'),
        'last_name': request.data.get('last_name'),
        'first_name': request.data.get('first_name'),
        'phone': request.data.get('phone'),
        'profession': request.data.get('profession'),
        'bio': request.data.get('bio'),
        'status': statusAccount,
    }

    # Create the user
    serializer = UsersSerializerAdd(data=new_user)
    if serializer.is_valid():
        serializer.save()
        return Response({
           'message': 'User successfully registered.',
           'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
           'message': 'Error while registering user.',
                'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    """
    Get all users.
    """
    if not PermissionChecker.has_permission(request, 'view_users'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user(request, id):
    """
    Get a specific user.
    """
    if not PermissionChecker.has_permission(request, 'view_users'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    user = get_object_or_404(Users, id=id)
    serializer = UsersSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def usersByRole(request, role_id):
    """
    Get all users by role.
    """
    if not PermissionChecker.has_permission(request, 'view_users'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    users = Users.objects.filter(role=role_id)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def sendInvitationToMentor(request):
    if not PermissionChecker.has_permission(request, 'can_send_invitation'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    mentor_id = request.data.get('mentor')
    mentee_id = request.data.get('protected')

    try:
        mentor = Users.objects.get(id=mentor_id, role__name=UserRoleEnum.MENTOR.value)
        mentee = Users.objects.get(id=mentee_id, role__name=UserRoleEnum.PROTECTED.value)
    except Users.DoesNotExist:
        return Response({'message': 'Mentor or Mentee not found or has the wrong role'}, status=status.HTTP_404_NOT_FOUND)

    existing_relation = Members.objects.filter(mentor=mentor, mentore=mentee)
    if existing_relation.exists():
        return Response({'message': 'A relationship already exists between Mentor and Mentee'}, status=status.HTTP_400_BAD_REQUEST)

    new_relation = Members(mentor=mentor, mentore=mentee)
    new_relation.save()

    return Response({'message': 'Invitation sent successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getMyInvitationSendMeList(request):
    user = request.user
    invitations_received = Members.objects.filter(mentor=user, status=False, mentor__role__name=UserRoleEnum.MENTOR.value)
    serializer = MembersSerializer(invitations_received, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getMyInvitationISend(request):
    user = request.user
    invitations_sent = Members.objects.filter(mentore=user, status=False, mentore__role__name=UserRoleEnum.PROTECTED.value)
    serializer = MembersSerializer(invitations_sent, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def validationInvitation(request):
    if not PermissionChecker.has_permission(request, 'can_validate_invitation'):
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    user = request.user
    invitation_id = request.data.get('invitation_id')

    try:
        invitation = Members.objects.get(id=invitation_id, mentor=user, status=False)
    except Members.DoesNotExist:
        return Response({'message': 'Invitation not found or already validated'}, status=status.HTTP_404_NOT_FOUND)

    invitation.status = True
    invitation.save()

    return Response({'message': 'Invitation validated successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def myMentorLists(request):
    user = request.user
    mentor_list = Members.objects.filter(mentore=user, status=True).values_list('mentor__id', flat=True)
    mentors = Users.objects.filter(id__in=mentor_list)

    serializer = UsersSerializer(mentors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def myMenteeLists(request):
    user = request.user
    mentee_list = Members.objects.filter(mentor=user, status=True).values_list('mentore__id', flat=True)
    mentees = Users.objects.filter(id__in=mentee_list)

    serializer = UsersSerializer(mentees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
