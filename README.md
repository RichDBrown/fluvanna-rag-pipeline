# HR Policy RAG Assistant
A Retrieval-Augmented Generation (RAG) application that answers questions using information retrieved from a collection of HR policy PDFs.

The project demonstrates the basic RAG pipeline: **PDFs → Text Extraction → Chunking → Embedding → Query → Semantic Search → Top K Chunks → LLM Response**

## 📋 Table of Contents
* [Prerequisites](#prerequisites)
* [macOS / Linux Guide](#macos--linux-guide)
* [Windows Guide](#windows-guide)

## Prerequisites
Before running the application, ensure your environment meets the following baseline requirements:

* **Target Environment:** Python 3.13 or Later

# macOS / Linux Guide
This guide walks you through how to setup the application on macOS or a Linux operating system.

## 🚀 Deployment Steps

### Step 1: Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Get a Gemini API Key
To use this application, you will need an API key from Google AI Studio.

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click **API Keys** in the top navigation or sidebar.
4. Select **Create API key** (you can create it in a new project or an existing Google Cloud project).
5. Copy your newly generated API key.

### Step 4: Configure Environment Variables
Create a `.env.local` file in the root directory of your project and add your key:
```env
GEM_AI_KEY=your_api_key_here
```

### Step 5: Run Application
Start the application from the root directory:
```bash
python main.py
```

# Windows Guide
This guide walks you through how to setup the application on Windows operating system.

## 🚀 Deployment Steps

### Step 1: Create a Virtual Environment
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 3: Get a Gemini API Key
To use this application, you will need an API key from Google AI Studio.

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click **API Keys** in the top navigation or sidebar.
4. Select **Create API key** (you can create it in a new project or an existing Google Cloud project).
5. Copy your newly generated API key.

### Step 4: Configure Environment Variables
Create a `.env.local` file in the root directory of your project and add your key:
```env
GEM_AI_KEY=your_api_key_here
```

### Step 5: Run Application
Start the application from the root directory:
```powershell
python main.py
```
