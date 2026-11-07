# FoodVision AI

**A personal Computer Vision learning project, built one experiment at a time.**

FoodVision AI explores practical applications of Computer Vision through four simple food image analysis applications. Built with Python and pretrained AI models, the project demonstrates how different AI capabilities can be implemented with approximately 30 lines of code (LOC) per application.

The project is developed in my spare time as a learning experiment. There is no fixed release schedule — just ideas, experiments, and occasional progress. Suggestions, feedback, and contributions are welcome!

## Project Roadmap

| Application | Computer Vision Task | Proposed AI Model | Status |
|---|---|---|---|
| FoodDetect | Image Classification | YOLO26n-cls | ✅ Completed |
| FoodDescribe | Image Captioning | Salesforce BLIP | 📋 Planned |
| FoodCounter | Object Detection | YOLO26n | 📋 Planned |
| FoodHealth | Image Segmentation | YOLO26n-seg | 📋 Planned |

*Model selections are experimental and may evolve as the project develops.*

## Current Application

### FoodDetect — Food Image Classification

FoodDetect uses a pretrained YOLO26n classification model to identify food categories in an uploaded image. It returns the top five predictions with confidence scores through a simple Gradio web interface.

![FoodDetect Application](fooddetect.png)

**Try it yourself:**

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/priandoyo/foodvision/blob/main/fooddetect.ipynb)

## Technology Stack

- **Programming Language:** Python
- **Development Environment:** Google Colab
- **Web Interface:** Gradio
- **AI Frameworks:** Ultralytics and Hugging Face Transformers
- **AI Models and approaches:** YOLO, Salesforce BLIP, CLIP, and Vision Transformers (ViT)

## Learning Objectives

- Explore practical Computer Vision applications.
- Experiment with pretrained AI models without training from scratch.
- Learn basic Python programming and AI integration.
- Use ChatGPT for prompt engineering and application development.
- Understand how simple Python code can become a working AI application.

## Development Progress

As of 7 November 2026, FoodDetect is the first completed application. FoodDescribe, FoodCounter, and FoodHealth remain on the roadmap.

See the [Development Log](devlog/) for project updates and experiments.

## Contributions and Ideas

This is a personal learning project, but collaboration is welcome!

Ideas, suggestions, model recommendations, code improvements, and contributions are appreciated. Whether you are an experienced developer or someone learning AI, feel free to explore the project and share your thoughts.

**Built for learning, curiosity, and fun.**

*One experiment at a time. No deadlines, just code.*
