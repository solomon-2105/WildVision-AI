# Nighttime Wildlife Detection using Zero-DCE++ and YOLOv8

This project implements a two-stage deep learning pipeline for detecting wildlife in nighttime environments. Low-light images are first enhanced using the **Zero-DCE++** model and then processed by **YOLOv8** for animal detection. The system is designed to improve visibility in dark highway or forest conditions and support real-time wildlife monitoring.

## Overview

Nighttime images captured on highways often suffer from low illumination, noise, motion blur, and glare from vehicle headlights. These factors reduce the performance of traditional computer vision systems. This project addresses the problem by separating the enhancement and detection stages.

1. **Zero-DCE++** improves image brightness and contrast using pixel-wise curve estimation.
2. **YOLOv8** detects wildlife objects from the enhanced images using an anchor-free detection architecture.

## Pipeline

Raw Image → Zero-DCE++ Enhancement → Image Resize (640×640) → YOLOv8 Detection → Bounding Boxes + Labels

## Features

- Low-light image enhancement using **Zero-DCE++**
- Anchor-free object detection using **YOLOv8**
- Real-time detection capability
- Multi-scale feature extraction
- Non-Maximum Suppression for duplicate removal
- Support for wildlife monitoring and highway safety systems

## Dataset

The model was trained on the **NTLNP Wildlife Detection Dataset**.

Dataset Link:  
https://huggingface.co/datasets/myyyyw/NTLNP

Dataset details:
- 25,657 infrared wildlife images
- 17 animal categories
- Pascal VOC annotation format
- Image resolutions include 1280×720 and 1600×1200

## Model Training

Training configuration:

- Input resolution: 640×640
- Epochs: 100
- Optimizer: AdamW
- Loss functions:
  - Box Loss
  - Classification Loss
  - Distribution Focal Loss (DFL)

## Evaluation Metrics

Model performance is evaluated using:

- Precision
- Recall
- mAP@0.5
- mAP@0.5–0.95

## Results

Final model performance:

- Precision: **0.974**
- Recall: **0.955**
- mAP@0.5: **0.976**
- mAP@0.5–0.95: **0.857**

The results show that combining Zero-DCE++ enhancement with YOLOv8 detection significantly improves wildlife detection accuracy in low-light environments.

## Applications

- Highway wildlife monitoring
- Road safety systems
- Smart transportation systems
- Nighttime wildlife surveillance
- Camera trap monitoring
