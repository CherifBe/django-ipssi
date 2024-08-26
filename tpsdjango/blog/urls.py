from django.urls import path
from .views import UserListCreate, UserRetrieveUpdateDestroy, ArticleListCreate, ArticleRetrieveUpdateDestroy, CommentListCreate, CommentRetrieveUpdateDestroy
 
urlpatterns = [
#    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('users/', UserListCreate.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view()),
    path('articles/', ArticleListCreate.as_view()),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroy.as_view()),
    path('comments/', CommentListCreate.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view()),
]