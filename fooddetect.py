# FOODDETECT AI - Fast YOLO Classification

from ultralytics import YOLO
import gradio as gr

# Load pretrained AI model
model = YOLO("yolo26n-cls.pt")

# Food classification
def detect_food(image):

    if image is None:
        return "Please upload a food image."

    result = model.predict(
        image,
        imgsz=224,
        verbose=False
    )[0]

    output = ""

    for class_id, confidence in zip(
        result.probs.top5,
        result.probs.top5conf
    ):
        food = result.names[class_id]
        output += f"{food}: {float(confidence):.2%}\n"

    return output

# Create website
app = gr.Interface(
    fn=detect_food,
    inputs=gr.Image(type="pil", label="Upload Food Image"),
    outputs=gr.Textbox(label="Classification Results"),
    title="FoodDetect AI",
    description="Fast AI-powered food image classification using YOLO."
)

app.launch(share=True)
