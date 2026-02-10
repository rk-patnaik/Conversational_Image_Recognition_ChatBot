# Image-Based Conversational AI using BLIP

A CPU-based conversational AI system that understands images and answers user questions using a vision–language transformer model (BLIP).


# Features
- Image caption generation
- Visual Question Answering (VQA)
- Conversational interaction
- CPU-only execution
- Runs in Google Colab or local Python environment


# Overview
This project allows users to upload an image, receive an automatic caption, and ask natural language questions about the image. The system uses the BLIP VQA model, which combines a Vision Transformer and text transformer to jointly process visual and textual information.


# Workflow
1. User uploads an image
2. Model generates an initial caption
3. User asks questions about the image
4. Model answers using image + text context
5. Conversation continues for the same image


# Tech Stack
- Python
- PyTorch
- Hugging Face Transformers
- BLIP (Vision–Language Model)
- PIL (Image Processing)

