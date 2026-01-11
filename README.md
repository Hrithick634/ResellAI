# 📱 AI-Based Mobile Damage Detection & Resale Price Estimation

An end-to-end **AI-powered web application** that estimates the **resale value of smartphones** using **computer vision, deep learning, and machine learning**. The system analyzes phone images and hardware specifications to deliver accurate, real-time resale pricing.

---

## 🚀 Features

- 📸 **Image-based damage detection** using CNN (ResNet50)
- 🔍 **Screen presence validation** using YOLO object detection
- 📊 **Spec-based depreciation modeling** using machine learning regression
- 💰 **Dynamic resale value estimation** (20–80% of MRP)
- ⚡ **Low-latency inference** (≈41.8 ms per image)
- 🌐 **Full-stack deployment** with React frontend and FastAPI backend

---

## 🧠 AI Models Used

| Component | Model | Performance |
|---------|------|-------------|
| Screen Damage Classification | ResNet50 (CNN) | 82% accuracy |
| Screen Detection | YOLO | 73% accuracy |
| Spec Depreciation | ML Regression | Real-valued output |
| Inference Time | Optimized Pipeline | 41.8 ms (single image) |

---

## 🏗️ System Architecture

Frontend (React)
|
v
FastAPI Backend
|
├── YOLO → Screen Detection
├── CNN → Damage Classification
├── ML Model → Spec Depreciation
└── Pricing Engine → Final Resale Value


---

## 🛠️ Tech Stack

**Frontend**
- React.js
- Axios
- HTML / CSS

**Backend**
- FastAPI
- TensorFlow / Keras
- YOLO (Ultralytics)
- NumPy
- Python

**ML / DL**
- CNN (ResNet50)
- Object Detection (YOLO)
- Feature Engineering
- Regression Modeling

---

## 📂 Project Structure

Damage_classification/
│
├── frontend/ # React UI
├── backend/ # FastAPI + ML services
├── CNN/ # Trained CNN models
├── YOLO/ # YOLO weights
├── datasets/
└── README.md


---

## 🧪 Example Output

- Damage Class: `moderately_broken`
- Damage Score: `0.63`
- Spec Depreciation: `0.42`
- Estimated Resale Value: `₹18,400`

---

## 📌 Use Cases

- Online mobile resale platforms
- Automated device inspection systems
- AI-powered pricing engines
- Computer vision learning projects

---

## 👤 Author

**Hrithick Kanagaraj**  
B.Tech – Metallurgy & Materials Science  
AI | Machine Learning | Computer Vision  

---