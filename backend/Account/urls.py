from django.urls import path
from Account.Views.views_authenticate import *
from Account.Views.views import *
from Account.Views.general_views import *
from Account.Views.views_user_stack import *

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('token/refresh', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('logout', Logout.as_view(), name='logout'),
    path('register', register, name='register'),
    path('users', users, name='users'),
    path('users/<int:id>', user, name='user'),
    path('users-by-role/<int:role_id>', usersByRole, name='users_by_role'),
    path('send-invitation', sendInvitationToMentor, name='send_invitation'),
    path('validate-invitation', validationInvitation, name='validate_invitation'),
    path('my-invitations-received', getMyInvitationSendMeList, name='my-invitations-received'),
    path('my-invitations-sent', getMyInvitationISend, name='my-invitations-sent'),

    path('my-mentor-list', myMentorLists, name='my_mentor_list'),
    path('my-mentee-list', myMenteeLists, name='my_mentee_list'),

    path('countries', countries, name='countries'),
    path('professions', professions, name='professions'),
    path('stacks', stacks, name='stacks'),


    # Stacks
    path('add-user-stacks', createUserStack, name='add_user_stacks'),
    path('delete-user-stacks', deleteUserStacks, name='delete_user_stacks'),
]