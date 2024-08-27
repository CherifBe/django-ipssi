from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import TextAnalysis
from .serializers import TextAnalysisSerializer
from .nlp import analyze_sentiment
 
class TextAnalysisListCreate(generics.ListCreateAPIView):
    queryset = TextAnalysis.objects.all()
    serializer_class = TextAnalysisSerializer
    permission_classes = [IsAuthenticated]
 
    def perform_create(self, serializer):
        sentiment = analyze_sentiment(self.request.data['text'])
        serializer.save(author=self.request.user, sentiment=sentiment)