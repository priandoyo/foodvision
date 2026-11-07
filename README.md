
# FoodVision AI

FoodVision AI is a beginner-friendly **Computer Vision** project featuring four food image analysis applications. Built with Python and pretrained AI models, each application demonstrates a different computer vision capability using approximately 30 lines of code (LOC).

## Food Image Analysis Applications

| Application | Use Case | AI Task | Pretrained Model |
|---|---|---|---|
| **FoodDetect** | Identify food categories, e.g. burger or pizza | Image Classification | YOLO26n-cls, Nateraw Food (ViT) |
| **FoodDescribe** | Describe visible food, e.g. burger with lettuce | Image Captioning | Salesforce BLIP |
| **FoodCounter** | Locate and count food items in an image | Object Detection | YOLO26n |
| **FoodHealth** | Identify food regions for composition analysis | Image Segmentation | YOLO26n-seg |

The project explores pretrained models and approaches including **YOLO, Salesforce BLIP, CLIP, and Vision Transformers (ViT)**.

## FoodDetect – Image Classification

FoodDetect is the first ready-to-run application in this workshop. It uses YOLO26n-cls to classify food images and return the top five predictions with confidence scores.

### Application Screenshot

![FoodDetect AI Application](fooddetect.png)

### Try FoodDetect in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/priandoyo/foodvision/blob/main/fooddetect.ipynb)

### How to Run

1. Open FoodDetect using the Google Colab link above.
2. Select **File → Save a copy in Drive**.
3. Run the notebook.
4. Upload a food image.
5. Review the AI classification results.

## Workshop Approach

Participants are encouraged to use ChatGPT to generate, understand, and experiment with Python code. Ready-to-run notebooks are also provided as starter templates for participants who need additional assistance.

## Repository Structure

```text
foodvision/
├── README.md
├── fooddetect.ipynb
└── fooddetect.png
```

More application notebooks will be added as the project expands.

## Technical Note

Image segmentation identifies food regions but does not independently calculate calories, fat, or protein. Nutritional estimation requires additional food recognition, portion estimation, and nutritional reference data.
