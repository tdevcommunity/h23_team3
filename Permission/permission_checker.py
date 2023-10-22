from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions
from Account.models import Users
from Permission.models import Permission_roles

def extract_user_id_from_token(request):
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(' ')[1]
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(auth_token)
            return validated_token['user_id']
        else:
            raise exceptions.AuthenticationFailed('Authorization header missing')
    except Exception as e:
        raise exceptions.AuthenticationFailed('Invalid token')
    
class PermissionChecker:
    def has_permission(request, permission_key):
        user_id = extract_user_id_from_token(request)
        try:
            user = Users.objects.get(id=user_id)
            if user.status == False:
                raise PermissionDenied('User is inactive')
            user_role = user.role 
            permission = Permission_roles.objects.filter(role=user_role, permission__permission_key=permission_key)
            if permission.exists():
                return True
        except Users.DoesNotExist:
            pass
        return False