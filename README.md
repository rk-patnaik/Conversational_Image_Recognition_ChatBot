# Conversational Image Recognition Chat Bot

A production-ready multimodal AI system that understands images and answers natural language questions using a vision–language transformer model. The system performs image captioning and visual question answering (VQA) and is optimized to run on CPU-only environments.


# Features

- Image caption generation
- Visual Question Answering (VQA)
- Conversational interaction with images
- CPU-optimized inference (no GPU required)
- Clean, modular, and scalable architecture


# Project Overview

Traditional image processing systems are limited to classification or object detection and do not support natural interaction. This project bridges that gap by enabling users to upload an image, receive an automatic description, and ask follow-up questions about the image in natural language.

The system is built using the BLIP (Bootstrapped Language–Image Pretraining) model, which combines vision and language understanding in a single unified framework.


# System Architecture

The system follows a four-layer architecture:

1. User Interface Layer – Image upload and question input  
2. Preprocessing Layer – Image resizing and normalization  
3. BLIP Model Layer – Vision Transformer + Text Transformer + Decoder  
4. Output Layer – Caption and answer generation  


# Technologies Used

- Programming Language: Python  
- Deep Learning Framework: PyTorch  
- Model: BLIP (Vision–Language Transformer)  
- Libraries: Hugging Face Transformers, PIL, OpenCV  
- Hardware: CPU-based inference  


# Dataset & Evaluation

- Datasets used: COCO
- Evaluation metrics:
  - BLEU, METEOR, CIDEr for image captioning
  - VQA Accuracy for question answering
- Achieved ~82–84% accuracy on VQA tasks

