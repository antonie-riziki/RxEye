# RxEye 🧠💊

**RxEye** is an AI-powered health-tech solution that lets users **scan, identify, and understand medicines instantly** using image recognition and Retrieval-Augmented Generation (RAG). Built to promote safer medication practices, RxEye combines Machine Learning, OCR, and Natural Language Processing to deliver accurate drug information and personalized insights.

---

## 🔍 Key Features

- **Medicine Image Recognition**  
  Upload an image of a pill, box, or blister — RxEye identifies the medicine and displays detailed information including dosage, side effects, and usage.

- **RAG-based Q&A Assistant**  
  Ask questions like “Can I take this while pregnant?” and get instant, AI-generated answers sourced from verified drug databases.

- **Barcode & Label OCR Scanner**  
  Automatically extract data from medicine packaging and prescriptions using Optical Character Recognition.

- **Symptom Checker & Recommendation**  
  Input your symptoms and receive medicine suggestions (with caution and disclaimer).

- **Personal Medication Tracker**  
  Save medicines, set reminders, and monitor your medication journey.

- **Fake Drug Detection (Coming Soon)**  
  Use packaging patterns, metadata, and user location to flag suspected counterfeit drugs.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit / React (optional for full app)
- **Backend:** FastAPI / Flask
- **Image Recognition:** PyTorch / TensorFlow + EfficientNet / CLIP
- **OCR:** Tesseract / Google Vision API
- **RAG:** LangChain + FAISS + OpenAI / HuggingFace LLMs
- **Voice:** Whisper (for speech input)
- **SMS Alerts:** Africa's Talking API

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/rxeye.git
cd rxeye
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Folder Structure

```
rxeye/
│
├── app.py                 # Main Streamlit app
├── model/                 # ML models (image classification, OCR)
├── rag/                   # Retrieval-Augmented Generation pipeline
├── data/                  # Sample images, drug info
├── utils/                 # Helper functions
└── requirements.txt       # Dependencies
```

---

## 🤖 AI Models

- Custom-trained CNN for pill recognition (EfficientNet/ResNet)
- OCR engine for text extraction from packages
- LangChain-powered RAG assistant with drug Q&A capabilities

---

## 🧠 Sample Use Cases

- Upload a drug image to identify it
- Ask: "Can I mix this with ibuprofen?"
- Scan a prescription and extract dosage info
- Get reminders via SMS to take your meds

---

## 📄 License

MIT License — feel free to fork and build upon RxEye for community good.

---

## 🤝 Contributing

We welcome issues and pull requests! Please follow the contributing guidelines.

---

## 📬 Contact

Built with ❤️ during the [Africa’s Talking Health-Tech Hackathon](https://community.africastalking.com/events/).

> _RxEye: Your digital eye for medicine safety._
