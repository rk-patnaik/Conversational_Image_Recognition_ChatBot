import torch
from transformers import BlipProcessor, BlipForQuestionAnswering

MODEL_NAME = "Salesforce/blip-vqa-base"
DEVICE = "cpu"

print(f"Loading BLIP VQA model on {DEVICE}...")

processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForQuestionAnswering.from_pretrained(MODEL_NAME).to(DEVICE)
model.eval()

print("Model loaded successfully!")


def ask_blip(image, question=None):
    """
    Generates caption or answers a question about an image.
    """
    if question:
        inputs = processor(image, question, return_tensors="pt").to(DEVICE)
    else:
        prompt = "a picture of"
        inputs = processor(image, prompt, return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=50)

    return processor.decode(output[0], skip_special_tokens=True)
