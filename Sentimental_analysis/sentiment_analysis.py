import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from emotion_lexicon import emotion_lexicon

def analyze_overall_emotion(text, emotion_lexicon):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    
    # Find the emotion with the highest intensity
    max_emotion = max(sentiment_scores, key=lambda key: sentiment_scores[key])
    
    return max_emotion

def analyze_detailed_emotions(text, emotion_lexicon):
    # Analyze emotions based on the emotion lexicon
    emotion_counts = {emotion: 0 for emotion in emotion_lexicon.keys()}
    for word, emotions in emotion_lexicon.items():
        for emotion in emotions:
            if emotion in text.lower():
                emotion_counts[word] += 1
    
    return emotion_counts

def main():
    # Get input text from user
    text = input("Enter some text: ")
    
    # Analyze overall emotion
    overall_emotion = analyze_overall_emotion(text, emotion_lexicon)
    print(f'Overall emotion: {overall_emotion.capitalize()}')
    
    # Ask the user if they want a more detailed breakdown of emotions
    choice = input("Do you want a more detailed breakdown of emotions? (yes/no): ")
    if choice.lower() == 'yes':
        # Analyze detailed emotions
        detailed_emotions = analyze_detailed_emotions(text, emotion_lexicon)
        print("Detailed breakdown of emotions:")
        for emotion, count in detailed_emotions.items():
            print(f'{emotion.capitalize()}: {count}')

if __name__ == "__main__":
    # Download NLTK resources
    nltk.download('vader_lexicon')
    
    # Run the main function
    main()
