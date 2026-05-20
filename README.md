<div align="center">

# 🚀 JARVIS AI
### Unified AI-Powered Productivity Ecosystem

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/AI-LLM%20Powered-black?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/RAG-Enabled-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Development-orange?style=for-the-badge"/>

<br/>

> An all-in-one AI ecosystem that combines Conversational AI, AI Coding Assistant, Prompt Engineering, RAG-based PDF Chatbot, AI Resume Analysis, AI Image Generation, and Productivity Tools into a single scalable platform.

</div>

---

# 📌 Overview

Modern AI systems are fragmented across multiple platforms.

Users often need:
- One platform for coding
- Another for image generation
- Another for PDF interaction
- Another for ATS resume analysis
- Another for AI communication

This increases:
- ❌ Cost
- ❌ Workflow switching
- ❌ Complexity
- ❌ Productivity loss

## ✅ Solution

**JARVIS AI** solves this problem by integrating multiple AI-powered utilities into a single centralized ecosystem.

The platform is designed for:
- 🎓 Students
- 💻 Developers
- 👨‍💼 Professionals
- 🎨 Content Creators
- 📚 Researchers

---

# ✨ Core Features

---

## 🎙️ AI Assistant

A real-time conversational AI assistant with voice interaction support.

### 🔹 Features
- Speech-to-Text interaction
- Human-like conversation
- Text-to-Speech output
- Natural AI communication

### 🔹 Technologies
```python
llama-3.3-70b-versatile
edge-tts
SpeechRecognition
PyAudio
```

---

## 💻 Code/Debug

An AI-powered coding workspace for developers and students.

### 🔹 Features
- Integrated code editor
- AI code analysis
- Debugging support
- AI Co-pilot
- Code optimization
- Logic explanation

### 🔹 Workflow
```text
User Code
   ↓
AI Analysis
   ↓
Error Detection
   ↓
Suggestions & Optimization
   ↓
Final Output
```

### 🔹 Models Used
```python
ministral-8b-latest
mistral-small-latest
```

---

## 🎨 ImageLab

Generate AI-powered visuals from prompts.

### 🔹 Capabilities
- Realistic image generation
- Anime generation
- Cinematic visuals
- Wallpapers
- Product concepts
- AI artworks

### 🔹 API Used
```python
https://image.pollinations.ai
```

---

## 🧩 PromptLab

An intelligent AI prompt engineering workspace.

### 🔹 Generate Prompts For
- AI Agents
- Coding
- YouTube Content
- SEO
- Marketing
- Automation
- Resume Generation
- Business Strategy
- Startup Ideas
- LLM System Prompts

### 🔹 Model Used
```python
Gemini
```

---

## 📚 Jarvis Scholar

AI-powered educational productivity system.

### 🔹 Smart PDF Chatbot
Upload PDFs and interact with them naturally using RAG architecture.

### 🔹 Features
- Context-aware responses
- Semantic retrieval
- PDF understanding
- Exam preparation
- Intelligent revision

---

### 🔹 AI Note Summarizer
Convert rough notes into structured study material.

### 🔹 Features
- AI summarization
- Key point generation
- Clean formatting
- Downloadable PDF notes

---

## 🔍 RAG Architecture

The system uses **Retrieval-Augmented Generation (RAG)**.

### 🔹 Workflow

```text
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
ChromaDB Storage
   ↓
Semantic Retrieval
   ↓
LLM Response
```

### 🔹 Models Used

#### LLMs
```python
command-r-08-2024
command-a-03-2025
```

#### Embedding Model
```python
sentence-transformers/all-MiniLM-L6-v2
```

---

## 📄 SmartCV

AI-powered resume and ATS optimization workspace.

### 🔹 Resume Builder
- AI-assisted resume generation
- Professional formatting
- Role-based customization
- Export functionality

### 🔹 ATS Resume Analyzer
- ATS compatibility scoring
- Keyword optimization
- Resume analysis
- Recruiter visibility enhancement

---

# 🏗️ System Architecture

The platform follows a modular AI ecosystem architecture.

```text
Frontend Layer
      ↓
Backend Layer
      ↓
AI Processing Layer
      ↓
Database Layer
      ↓
Vector Retrieval Layer
      ↓
LLM Response Generation
```

---

# ⚙️ Tech Stack

## 🖥️ Main Language
```python
Python
```

---

## 📦 Libraries Used

```python
python-dotenv
requests
edge-tts
SpeechRecognition
streamlit
pyaudio
Pillow
cohere
google-genai
groq
mistralai
pymongo
mysql-connector-python
streamlit-monaco
langchain
langchain-community
langchain-text-splitters
langchain-chroma
chromadb
sentence-transformers
pypdf
```

---

# 🤖 AI Models

| Purpose | Model |
|---|---|
| Conversational AI | llama-3.3-70b-versatile |
| Code Analysis | ministral-8b-latest |
| AI Co-Pilot | mistral-small-latest |
| Prompt Engineering | Gemini |
| Educational AI | command-r-08-2024 |
| Educational AI | command-a-03-2025 |

---

# 🗄️ Database Architecture

| Database | Purpose |
|---|---|
| MySQL | Structured Data |
| MongoDB | Unstructured Data |
| ChromaDB | Vector Embeddings |

---

# 📂 Project Structure

```bash
Ahonix_AI/
│
├── Assets/
│   └── pdf/
│
├── Backend/
│   │
│   ├── Config/
│   │   ├── __init__.py
│   │   ├── models.yaml
│   │   └── settings.py
│   │
│   ├── Core/
│   │   └── Features/
│   │       ├── LLMModelCore/
│   │       ├── pdfGenerator/
│   │       ├── RagPipeLine/
│   │       └── ResumeBuilder/
│   │
│   ├── Features/
│   │   ├── Account.py
│   │   ├── CodeEditor.py
│   │   ├── Image.py
│   │   ├── PromptEng.py
│   │   ├── Resume.py
│   │   └── Scholar.py
│   │
│   ├── Services/
│   │   ├── modelGemini.py
│   │   ├── modelMistral.py
│   │   ├── modelCohere.py
│   │   └── modelLLaMa.py
│   │
│   ├── DB/
│   │   ├── MongoDB/
│   │   ├── MySQL/
│   │   └── ChromaDB/
│
├── Frontend/
│
├── Prompt/
│
├── Tests/
│
├── .env
├── .gitignore
└── venv/
```

---

# 🔄 General Workflow

```text
User Input
   ↓
Frontend Interface
   ↓
Backend Processing
   ↓
AI Model Execution
   ↓
Database / Vector Retrieval
   ↓
AI Response Generation
   ↓
Response Returned to User
```

---

# 📈 Advantages

✅ Centralized AI ecosystem  
✅ Reduced dependency on multiple platforms  
✅ Cost-effective productivity system  
✅ AI-assisted learning & development  
✅ Semantic document understanding  
✅ Voice-based interaction  
✅ Resume optimization support  
✅ Scalable architecture  

---

# 🚧 Challenges Faced

- Multi-LLM integration
- RAG optimization
- Semantic retrieval tuning
- Latency handling
- Prompt engineering optimization
- Hybrid database management

---

# 🔮 Future Scope

Future versions may include:

- 🤖 Multi-Agent AI Systems
- 📱 Mobile Application
- ☁️ Cloud Deployment
- 🧠 AI Memory Systems
- 🎥 Video Understanding AI
- 🗣️ Advanced Voice Assistant
- 👥 Real-Time Collaboration
- ⚡ Autonomous AI Workflows

---

# 🧪 Testing

Current testing modules include:

```python
DocMindTest.py
homePageTest.py
IngestionPipeLine.py
RetrievalPipeLine.py
```

---

# 📜 License

This project is developed for:
- Educational Purposes
- Research Purposes
- AI Productivity Development

---

# 👨‍💻 Developer

<div align="center">

## Arijit Das

AI Engineer • Python Developer • Generative AI Enthusiast

</div>

---

# ⭐ Vision

> “Build an affordable all-in-one AI ecosystem capable of helping students, developers, professionals, and creators through intelligent automation and unified AI accessibility.”

---

<div align="center">

### 🌟 JARVIS AI — The Future of Unified AI Productivity

</div>
