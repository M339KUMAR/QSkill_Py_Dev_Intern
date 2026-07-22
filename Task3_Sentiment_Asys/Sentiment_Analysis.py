
from textblob import TextBlob


def analyze_sentiment(text: str) -> dict:
    
    """
    Analyzes the sentiment of a given text string using TextBlob.
    """

    # Create a TextBlob object
    blob = TextBlob(text)

    # Extract polarity and subjectivity scores
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
   
    # Determine the classification label based on the 
    # polarity score

    if polarity > 0 :
       classification = "Positive"

    elif polarity < 0:
       classification = "Negative"
   
    else:
       classification = "Neutral"

    return {
             "text": text,
             "polarity": round(polarity, 2),
             "subjectivity": round(subjectivity, 2),
             "classification": classification
           }

# --- Example Usage ---

# 1. Single text evaluation
sample_text = "I Joined QSkill Python Development Internship, To develop my Programming Skills & Work Experience."
result = analyze_sentiment(sample_text)

print("--- Single Text Analysis ---")
print(f"Text: '{result['text']}'")
print(f"Polarity: {result['polarity']} (Ranges from -1.0 to 1.0)")
print(f"Subjectivity: {result['subjectivity']} (Ranges from 0.0 to 1.0)")
print(f"Overall Label: {result['classification']}\n")


# 2. Batch processing multiple text samples
phrases = [
    "This was the worst movie I have ever watched. A complete waste of time.",
    "The train arrives at 3:00 PM tomorrow afternoon.",
    "I am not sure how I feel about the new update, but it looks decent."
]

print("--- Batch Text Analysis ---")
for phrase in phrases:
    analysis = analyze_sentiment(phrase)
    print(f"[{analysis['classification']}] (Pol: {analysis['polarity']}, Subj: {analysis['subjectivity']}) -> {analysis['text']}")
