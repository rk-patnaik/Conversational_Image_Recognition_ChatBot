from PIL import Image
from utils.blip_utils import ask_blip
from google.colab import files
from io import BytesIO

last_image = None


def process_uploaded_file(uploaded):
    global last_image
    last_image = None

    if not uploaded:
        print("🤖 Bot: No file selected.")
        return

    filename = list(uploaded.keys())[0]

    try:
        image_bytes = uploaded[filename]
        raw_image = Image.open(BytesIO(image_bytes)).convert("RGB")
        last_image = raw_image

        print("\n🤖 Bot: Image received. Generating description...")
        caption = ask_blip(raw_image)

        print(f"\n✨ Bot (Caption): {caption.capitalize()}.")
        print("\n➡️ Ask a question about the image.")
        print("Type 'upload' for new image or 'quit' to exit.")

    except Exception as e:
        print(f"Error processing image: {e}")
        last_image = None


print("\n--- Image-Based Conversational AI is Ready ---")
print("🤖 Bot: Type 'upload' to upload an image.")

while True:
    user_input = input("\n👤 You: ").strip()

    if user_input.lower() == "quit":
        print("🤖 Bot: Goodbye!")
        break

    elif user_input.lower() == "upload":
        uploaded = files.upload()
        process_uploaded_file(uploaded)

    elif last_image is not None:
        print("🤖 Bot: Processing your question...")
        try:
            answer = ask_blip(last_image, question=user_input)
            print(f"\n💬 Bot (Answer): {answer.capitalize()}.")
        except Exception as e:
            print(f"Error: {e}")

    else:
        print("🤖 Bot: Please upload an image first by typing 'upload'.")
