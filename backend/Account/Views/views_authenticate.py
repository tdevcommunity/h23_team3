from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.views import TokenRefreshView
from Account.models import Users
from Account.serializers import UsersSerializer
from BaseApi.Helper import isEmailOrPhone

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UsersSerializer
    def post(self, request):
        identify = request.data.get('identify')
        password = request.data.get('password')

        try:
            if isEmailOrPhone(identify) == 1:
                user = Users.objects.get(email=identify)
            elif isEmailOrPhone(identify) == 2:
                user = Users.objects.get(phone=identify)
            else:
                return Response({'message': 'Please provide an email or phone number.'}, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response({'message': 'Incorrect email/phone or password!'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'message': 'Incorrect email/phone or password!'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.status:
            return Response({'message': 'Inactive user account. Please contact the administrator if you think this is an error.'}, status=status.HTTP_400_BAD_REQUEST)
  
        refresh = RefreshToken.for_user(user)
        user.token = str(refresh.access_token)
        user.save()

        response = {
            'message': 'Welcome! Successfully connected.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': self.serializer_class(user).data
        }

        return Response(response, status=status.HTTP_200_OK)

class UserTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = self.user
            return Response({
                'refresh': str(response.data.get('refresh')),
                'access': str(response.data.get('access')),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'phone': user.phone,
                }
            })
        return response

class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
