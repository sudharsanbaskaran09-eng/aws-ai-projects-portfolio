import boto3
import json

# Initialize AWS clients
s3_client = boto3.client('s3', region_name='us-east-1')

        print(f"\n[{i}] {text[:60]}")
        response = comprehend_client.detect_sentiment(
            Text=text,
            LanguageCode='en'
        )
        results.append({
            'text': text,
            'sentiment': response['Sentiment'],
            'scores': r
    print(f"\n☁️ Results saved to S3: results/{filename}")

# ---- MAIN ----
if __name__ == "__main__":
    # Single text test
    single_text = "I absolutely love this product! Amazing quality and super fast delivery!"
    analyze_sentiment(single_text)

    # Multiple customer reviews
    reviews = [
        "Best purchase ever! Totally worth every penny!",
        "Terrible product. Broke after one day. Very disappointed.",
        "It is okay. Nothing special but gets the job done.",
        "Absolutely fantastic! Will definitely buy again!",
        "Worst customer service ever. Never buying from here again."
    ]

    results = analyze_multiple_texts(reviews)
    save_results_to_s3(results, 'sentiment_results.json')
