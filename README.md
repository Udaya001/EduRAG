# EduRAG: Intelligent Tutor Using RAG and LangChain

## Overview
EduRAG is an AI-powered tutoring system that uses Retrieval-Augmented Generation (RAG), LLM APIs, and PostgreSQL to deliver smart, context-aware educational responses.

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/Udaya001/edurag.git 
   cd edurag
2. Install dependencies
   ```bash
   pip install -r requirements.txt
4. Set up environment variables:
   ```bash
   cp .env.example .env
6. Run the server:
   ```bash
   uvicorn app.utils.main:app --reload
