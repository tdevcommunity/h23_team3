from django.contrib.auth.models import Permission
from BaseApi.AppEnum import UserRoleEnum 
from Permission.models import Permission_roles, Roles
from django.contrib.auth.models import Permission

permissionCodeNameForRole = [
    {
        "role": UserRoleEnum.MENTOR.value,
        "permissionCodeName": [
            "view_pays",
            "view_professions",
        ]
    },
    {
        "role": UserRoleEnum.PROTECTED.value,
        "permissionCodeName": [
            "view_pays",
            "view_professions",
        ]
    }
]

def affect_permission_to_role():
    superUserRole = Roles.objects.filter(name=UserRoleEnum.SUPER_ADMIN.value).first()
    permissions = Permission.objects.all()
    for permission in permissions:
        permission_roles, created = Permission_roles.objects.get_or_create(permission=permission, role=superUserRole)
        if created:
            permission_roles.save()
    
    for permissionCodeName in permissionCodeNameForRole:
        role = Roles.objects.filter(name=permissionCodeName["role"]).first()
        for permissionCodeName in permissionCodeName["permissionCodeName"]:
            permission = Permission.objects.filter(codename=permissionCodeName).first()
            permission_roles, created = Permission_roles.objects.get_or_create(permission=permission, role=role)
            if created:
                permission_roles.save()
   
    return True