# Resume Questionnaire Bot Using LLM
# Add your own OpenAI_API_KEY, env file is deleted
## Overview

The **Resume Questionnaire Bot** is a chatbot built with LangChain, FAISS, and Streamlit. It leverages advanced language models to answer questions about your resume in a conversational and interactive way. The bot reads and indexes my resume (PDF), allowing you to query its contents dynamically.

## Features

- **Resume-based Q&A**: Upload any resume and ask questions like "What are my skills?" or "What is my education?"
- **FAISS Vector Store**: Efficient local storage and retrieval of resume content using FAISS.
- **Interactive Chat Interface**: Built with Streamlit and `streamlit-chat` for an engaging user experience.
- **History-aware Retrieval**: Keeps track of chat history to provide contextually relevant answers.
- **Dynamic Updates**: Easily re-index your updated resume for new content.

---

## Installation

### Prerequisites
- Python 3.9 or higher
- `pip` or `conda` package manager

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/resume-questionnaire-bot.git
   cd resume-questionnaire-bot
