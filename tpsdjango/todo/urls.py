from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy, CustomAuthToken, SecureView, AdminOnlyView
 
urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('auth/', CustomAuthToken.as_view(), name='api_login'),
    path('secure/', SecureView.as_view(), name='test authentication'),
    path('admin/', AdminOnlyView.as_view(), name='admin only'),
]