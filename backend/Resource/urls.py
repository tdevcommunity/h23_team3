from django.urls import path
from Resource.Views.comment import *
from Resource.Views.resource_mini_blog import *
from Resource.Views.resource_question import *
from Resource.Views.resource_session import *

urlpatterns = [
    # Sessions
    path('create-session', createSession, name='create-session'),
    path('update-session/<int:resource_id>', updateSession, name='update-session'),
    path('delete-session/<int:resource_id>', deleteSession, name='delete-session'),
    path('get-session/<int:resource_id>', getSession, name='get-session'),
    path('my-mentor-sessions', getMyMentorSessions, name='my-mentor-sessions'),
    path('my-sessions', getMySessions, name='my-sessions'),
    path('sessions', getMySessions, name='sessions'),
    path('close-or-open-session/<int:resource_id>', closeOrOpenSession, name='close-or-open-session'),

    # Mini Blogs
    path('create-mini-blog', createMiniBlog, name='create-mini-blog'),
    path('update-mini-blog/<int:resource_id>', updateMiniBlog, name='update-mini-blog'),
    path('delete-mini-blog/<int:resource_id>', deleteMiniBlog, name='delete-mini-blog'),
    path('get-mini-blog/<int:resource_id>', getMiniBlog, name='get-mini-blog'),
    path('get-mini-blogs', getMiniBlogs, name='get-mini-blogs'),

    # Requests
    path('create-request', createRequest, name='create-request'),
    path('update-request/<int:resource_id>', updateRequest, name='update-request'),
    path('delete-request/<int:resource_id>', deleteRequest, name='delete-request'),
    path('get-request/<int:resource_id>', getRequest, name='get-request'),
    path('get-requests', getRequests, name='get-requests'),
    path('close-or-open-request/<int:resource_id>', closeOrOpenRequest, name='close-or-open-request'),

    # Discussions
    path('add-discussions/<int:ressource_id>', addDiscussions, name='add-discussions'),
    path('get-resource-discussions/<int:ressource_id>', getResourceDiscussions, name='get-resource-discussions'),
]