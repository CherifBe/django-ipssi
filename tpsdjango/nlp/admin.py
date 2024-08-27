from django.contrib import admin

from .models import TextAnalysis, TextClassification, TextPreprocessing

admin.site.register(TextAnalysis)
admin.site.register(TextClassification)
admin.site.register(TextPreprocessing)
# Register your models here.
