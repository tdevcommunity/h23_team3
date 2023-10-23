from django.urls import path
from Permission import views

urlpatterns = [
    path('roles/', views.roles, name='roles'),
    path('roles/create/', views.createRole, name='create_role'),
    path('roles/<int:id>/update/', views.updateRole, name='update_role'),
    path('roles/<int:id>/delete/', views.deleteRole, name='delete_role'),
    path('roles/<int:id>/', views.role, name='role'),
    path('roles/<int:role_id>/permissions/', views.rolePermissions, name='role_permissions'),
    path('roles/<int:role_id>/permissions/add/<int:permission_id>/', views.addPermissionToRole, name='add_permission_to_role'),
    path('roles/<int:role_id>/permissions/remove/<int:permission_id>/', views.removePermissionFromRole, name='remove_permission_from_role'),
]