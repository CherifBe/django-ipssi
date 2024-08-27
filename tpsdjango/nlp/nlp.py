from transformers import pipeline
 
# Load pre-trained model 
def analyze_sentiment(text):
    nlp_pipeline = pipeline("sentiment-analysis")
    result = nlp_pipeline(text)[0]
    return result['label']

def classify_text(text, candidate_labels):
    nlp_pipeline = pipeline("zero-shot-classification")
    result = nlp_pipeline(text, candidate_labels)
    return result['labels'][0]