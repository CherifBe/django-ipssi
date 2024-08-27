from rest_framework import serializers
from .models import TextAnalysis, TextClassification, TextPreprocessing
 
class TextAnalysisSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    sentiment = serializers.StringRelatedField(read_only=True)
 
    class Meta:
        model = TextAnalysis
        fields = ['id', 'text', 'sentiment', 'created_at', 'author']

class TextClassificationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TextClassification
        fields = ['id', 'text', 'category', 'created_at', 'author']

class TextPreprocessingSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    processed_text = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TextPreprocessing
        fields = ['id', 'raw_text', 'processed_text', 'created_at', 'author']
