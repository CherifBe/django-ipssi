from rest_framework import serializers
from .models import TextAnalysis
 
class TextAnalysisSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
 
    class Meta:
        model = TextAnalysis
        fields = ['id', 'text', 'sentiment', 'created_at', 'author']