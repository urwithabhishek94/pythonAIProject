# Jarvis AI Assistant

## Overview

Jarvis AI Assistant is a voice-enabled personal assistant developed in Python. It combines Speech Recognition, Text-to-Speech, Generative AI, and automation capabilities to perform various tasks through voice commands.

The project integrates a local Large Language Model (LLM) using Ollama and Qwen 2.5, allowing Jarvis to answer questions, maintain conversations, retrieve custom knowledge, and automate common tasks.

---

## Features

### Voice Interaction

* Speech-to-Text using SpeechRecognition
* Text-to-Speech using Windows SAPI
* Voice command execution

### AI Capabilities

* Conversational AI powered by Qwen 2.5 via Ollama
* Context-aware conversations
* Custom knowledge retrieval from text files
* Personalized responses

### Web Automation

* Open websites using voice commands
* Open Google, YouTube, Wikipedia, GitHub, LinkedIn, and more

### Information Retrieval

* Wikipedia search and summarization
* Personal knowledge base support
* Custom question answering from local files

### Utilities

* Play local music files
* Tell current time
* Launch desktop applications

---

## Technologies Used

* Python
* Ollama
* Qwen 2.5 LLM
* SpeechRecognition
* PyAudio
* PyWin32
* PyWhatKit
* Wikipedia API
* OpenRouter API (Optional)
* Python Dotenv

---

## Project Structure

```text
Jarvis-AI-Assistant/
│
├── jarvis.py
├── abhishek.txt
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
└── Openai/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Jarvis-AI-Assistant
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the Qwen model:

```bash
ollama pull qwen2.5:1.5b
```

Verify:

```bash
ollama run qwen2.5:1.5b
```

---

## Running the Project

```bash
python main.py
```

---

## Example Commands

* Open YouTube
* Open Google
* Open Wikipedia
* What is the time
* Play music
* Search Wikipedia for Python
* Tell me about Abhishek
* Tell me about Jarvis
* Who are you

---

## Custom Knowledge Base

Jarvis can answer questions from custom text files.

Example:

```text
Abhishek Gupta is a Software Developer.
He works at Incture Technologies.
He owns a Royal Enfield Hunter 350.
```

Users can ask:

* What does Abhishek do?
* Where does Abhishek work?
* Which bike does Abhishek own?

Jarvis retrieves information from the knowledge file and generates a response.

---

## Future Enhancements

* Weather information
* Email automation
* News summarization
* Local document search
* Face recognition
* Smart home integration
* Calendar and task management
* RAG-based knowledge retrieval
* Multi-language support

---

## Author

Abhishek Gupta

Software Developer | Python Developer | AI Enthusiast

This project was developed as a personal learning initiative to explore Generative AI, Large Language Models, Voice Assistants, and Automation using Python.
