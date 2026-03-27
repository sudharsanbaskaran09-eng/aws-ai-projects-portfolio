# Project 1 — AI Image Recognition App (AWS)

## 📌 Overview
This project is a **serverless AI-powered image recognition application** built on AWS.  
It analyzes images stored in Amazon S3 and detects objects, scenes, and labels using **Amazon Rekognition**.

Built as part of my **self-paced Cloud AI Architect learning journey**, this project demonstrates real-world integration of AI services with scalable cloud architecture.

---

## 🏗️ Architecture
User → API Gateway → Lambda → Rekognition → S3

---

## ⚙️ AWS Services Used
- **Amazon S3** — Stores input images  
- **Amazon Rekognition** — Performs image analysis (label detection)  
- **AWS Lambda** — Handles backend logic (serverless compute)  
- **Amazon API Gateway** — Exposes REST API endpoint  
- **AWS IAM** — Manages roles and permissions securely  

---

## 🚀 How It Works
1. User uploads an image to an S3 bucket  
2. API Gateway receives a POST request with image details  
3. Lambda function processes the request  
4. Rekognition analyzes the image  
5. Detected labels are returned as a JSON response  

---

## ▶️ How to Run
1. Clone this repository  
2. Configure AWS CLI with your credentials  
3. Upload an image to the S3 bucket (e.g., `uploads/` folder)  
4. Invoke the API using curl or Postman with the image name  
5. Receive AI-generated labels in JSON format  

---

## 📸 Screenshots
All screenshots are available in the `/screenshots` directory.

---

## 📈 Key Highlights
- Fully **serverless architecture** (no infrastructure management)  
- Real-time **AI-powered image analysis**  
- Scalable and cost-efficient design  
- Clean API-based integration  

---

## 🎯 Learning Outcome
- Hands-on experience with AWS AI services  
- Building end-to-end serverless applications  
- Understanding IAM roles and permissions in real projects  
- API integration with cloud-based AI  

---

## 👤 Author
**Sudharsan B**  

---

⭐ This is just the beginning of my Cloud AI journey — more advanced projects coming soon.
