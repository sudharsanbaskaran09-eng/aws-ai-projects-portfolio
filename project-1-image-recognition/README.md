# Project 1 — AI Image Recognition App (AWS)

An AI-powered cloud application that analyzes images and detects objects using AWS services.

---

## 🚀 Project Overview

This project demonstrates how to build a **serverless AI application** using AWS.

### Workflow:
1. Upload image to S3  
2. Trigger AI analysis using Rekognition  
3. Process via Lambda  
4. Access results via API  

---

## 🏗️ Architecture

- Amazon S3 → Stores images  
- AWS Lambda → Processes requests  
- Amazon Rekognition → Detects labels  
- API Gateway → Exposes REST API  

---

## ⚙️ Tech Stack

- Python (boto3)  
- AWS S3  
- AWS Rekognition  
- AWS Lambda  
- AWS API Gateway  

---

## 📂 Project Structure

project-1-image-recognition/
│
├── rekognition_app.py  
├── results.json  
└── README.md  

---

## 🔧 Setup Instructions

### 1. Configure AWS CLI
aws configure

### 2. Install Dependencies
pip install boto3

### 3. Run the App
python rekognition_app.py

---

## 🧪 API Testing

curl -X POST https://your-api-url/prod/analyze \
-H "Content-Type: application/json" \
-d '{"bucket": "your-bucket-name", "image": "test_image.jpg"}'

---

## 📸 Features

- Upload images to cloud  
- AI-based image recognition  
- JSON output with confidence scores  
- Serverless execution  
- REST API integration  

---

## 📚 Learning Outcomes

- AWS IAM & Security  
- Serverless Architecture  
- AI API Integration  
- Cloud Application Design  

---

## 📌 Future Improvements

- Web UI for uploads  
- Real-time processing  
- Face detection  
- Database integration (DynamoDB)  

---

## 👤 Author

Sudharsan B  


---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
