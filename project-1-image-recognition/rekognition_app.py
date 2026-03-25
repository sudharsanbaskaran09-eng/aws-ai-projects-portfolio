import boto3
import json

# Initialize AWS clients
s3_client = boto3.client('s3', region_name='us-east-1')
rekognition_client = boto3.client('rekognition', region_name='us-east-1')

# Your S3 bucket name
BUCKET_NAME = 'image-rekognition-brat'

def upload_image_to_s3(image_path, image_name):
    """Upload local image to S3"""
    print(f"📤 Uploading {image_name} to S3...")
    s3_client.upload_file(image_path, BUCKET_NAME, f'uploads/{image_name}')
    print(f"✅ Upload successful!")

def analyze_image(image_name):
    """Send image to Rekognition AI for analysis"""
    print(f"🤖 Analyzing image with Rekognition...")

    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': BUCKET_NAME,
                'Name': f'uploads/{image_name}'
            }
        },
        MaxLabels=10,
        MinConfidence=75
    )

    print("\n🎯 AI Detected:")
    print("-" * 40)
    for label in response['Labels']:
        print(f"  ✅ {label['Name']} — {label['Confidence']:.2f}%")

    # Save results locally
    with open('results.json', 'w') as f:
        json.dump(response['Labels'], f, indent=4)

    print("\n💾 Results saved to results.json")
    return response['Labels']

def save_results_to_s3(image_name):
    """Upload results back to S3"""
    result_file = image_name.replace('.jpg', '_results.json')
    s3_client.upload_file('results.json', BUCKET_NAME, f'results/{result_file}')
    print(f"☁️ Results saved to S3!")

# ---- MAIN ----
if __name__ == "__main__":
    IMAGE_PATH = "test_image.jpg"
    IMAGE_NAME = "test_image.jpg"

    upload_image_to_s3(IMAGE_PATH, IMAGE_NAME)
    analyze_image(IMAGE_NAME)
    save_results_to_s3(IMAGE_NAME)
