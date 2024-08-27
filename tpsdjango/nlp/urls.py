from django.urls import path
from .views import TextAnalysisListCreate
 
urlpatterns = [
    path('analyses/', TextAnalysisListCreate.as_view(), name='analysis-list-create'),
]