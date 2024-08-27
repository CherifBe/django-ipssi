from django.urls import path
from .views import TextAnalysisListCreate, TextClassificationListCreate, TextPreprocessingListCreate
 
urlpatterns = [
    path('analyses/', TextAnalysisListCreate.as_view(), name='analysis-list-create'),
    path('classifications/', TextClassificationListCreate.as_view(), name='classification-list-create'),
    path('preprocessings/', TextPreprocessingListCreate.as_view(), name='preprocessing-list-create'),
]