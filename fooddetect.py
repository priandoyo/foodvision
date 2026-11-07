{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# FOODDETECT AI - Fast YOLO Classification\n",
        "\n",
        "!pip install -q ultralytics gradio\n",
        "\n",
        "from ultralytics import YOLO\n",
        "import gradio as gr\n",
        "\n",
        "# Load lightweight YOLO classification model\n",
        "model = YOLO(\"yolo26n-cls.pt\")\n",
        "\n",
        "# Food classification\n",
        "def detect_food(image):\n",
        "\n",
        "    if image is None:\n",
        "        return \"Please upload a food image.\"\n",
        "\n",
        "    result = model.predict(\n",
        "        image,\n",
        "        imgsz=224,\n",
        "        verbose=False\n",
        "    )[0]\n",
        "\n",
        "    output = \"\"\n",
        "\n",
        "    for class_id, confidence in zip(\n",
        "        result.probs.top5,\n",
        "        result.probs.top5conf\n",
        "    ):\n",
        "        food = result.names[class_id]\n",
        "        output += f\"{food}: {float(confidence):.2%}\\n\"\n",
        "\n",
        "    return output\n",
        "\n",
        "# Create website\n",
        "app = gr.Interface(\n",
        "    fn=detect_food,\n",
        "    inputs=gr.Image(type=\"pil\", label=\"Upload Food Image\"),\n",
        "    outputs=gr.Textbox(label=\"Food Detection Results\"),\n",
        "    title=\"FoodDetect AI\",\n",
        "    description=\"Fast AI-powered food image classification using YOLO.\"\n",
        ")\n",
        "\n",
        "# Launch website\n",
        "app.launch(share=True)\n"
      ],
      "metadata": {
        "id": "KGznSQrDVHQc"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
