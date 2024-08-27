from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import TextAnalysis, TextClassification, TextPreprocessing
from .serializers import TextAnalysisSerializer, TextClassificationSerializer, TextPreprocessingSerializer
from .nlp import analyze_sentiment, classify_text
from .preprocessing import preprocess_text
 
class TextAnalysisListCreate(generics.ListCreateAPIView):
    queryset = TextAnalysis.objects.all()
    serializer_class = TextAnalysisSerializer
    permission_classes = [IsAuthenticated]
 
    def perform_create(self, serializer):
        sentiment = analyze_sentiment(self.request.data['text'])
        serializer.save(author=self.request.user, sentiment=sentiment)

class TextClassificationListCreate(generics.ListCreateAPIView):
    queryset = TextClassification.objects.all()
    serializer_class = TextClassificationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        candidate_labels = ["sports", "politics", "technology", "movie", "music", "art"]
        category = classify_text(self.request.data['text'], candidate_labels)
        serializer.save(author=self.request.user, category=category)


class TextPreprocessingListCreate(generics.ListCreateAPIView):
    queryset = TextPreprocessing.objects.all()
    serializer_class = TextPreprocessingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        processed_text = preprocess_text(self.request.data['raw_text'])
        serializer.save(author=self.request.user, processed_text=processed_text)
