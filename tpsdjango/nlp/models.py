from django.db import models
from django.contrib.auth.models import User
 
class TextAnalysis(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='analyses')
 
    def __str__(self):
        return self.text
    
class TextClassification(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classifications')

    def __str__(self):
        return self.text

class TextPreprocessing(models.Model):
    raw_text = models.TextField()
    processed_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preprocessings')

    def __str__(self):
        return self.raw_text