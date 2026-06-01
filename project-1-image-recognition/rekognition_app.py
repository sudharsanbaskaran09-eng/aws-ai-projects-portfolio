import boto3
import json

# Initialize AWS clients
s3_client = boto3.client('s3', region_name='us-east-1')
rekognition_client = boto3.client('rekognition', region_name='us-east-1')


def upload_image_to_s3(image_path, image_name):
    """Upload local image to S3"""
    print(f"📤 Uploading {image_name} to S3...")
    s3_client.upload_file(image_path, BUCKET_NAME, f'uploads/{image_name}')
    print(f"✅ Upload successful!")

def analyze_image(image_name):
    print(f"🤖 Analyzing i

    # Save results locally
    s3_client.upload_file('results.json', BUCKET_NAME, f'results/{result_file}')
    print(f"☁️ Results saved to S3!")

# ---- MAIN ----
if __name__ == "__main__":
    IMAGE_PATH = "test_image.jpg"
    IMAGE_NAME = "test_image.jpg"

    upload_image_to_s3(IMAGE_PATH, IMAGE_NAME)
    analyze_image(IMAGE_NAME)
    save_results_to_s3(IMAGE_NAME)
