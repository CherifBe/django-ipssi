from transformers import pipeline
 
# Load pre-trained model
nlp_pipeline = pipeline("sentiment-analysis")
 
def analyze_sentiment(text):
    result = nlp_pipeline(text)[0]
    return result['label']