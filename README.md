# WildVision-AI
### Zero-DCE++ + YOLOv8 Cascaded Pipeline

## Overview

This project presents a fully GPU-resident dual-network pipeline for high-speed nighttime object detection. The system integrates **Zero-DCE++** for low-light image enhancement with **YOLOv8** for object detection, enabling accurate wildlife detection under extremely low illumination conditions.

The entire training and inference workflow is engineered to remain on the GPU, eliminating CPU–GPU transfer bottlenecks and significantly improving throughput.

---

## Motivation

Nighttime object detection suffers from:

- Severe illumination degradation  
- Loss of feature detail  
- Poor detection confidence  
- Inference latency caused by preprocessing overhead  

This project addresses these limitations by:

1. Enhancing low-light frames using Zero-DCE++  
2. Passing enhanced frames directly to YOLOv8  
3. Maintaining full GPU memory residency throughout the pipeline  

---

## Architecture

Input Image (Low-Light)  
→ Zero-DCE++ (Low-Light Enhancement)  
→ Enhanced Image (GPU Memory)  
→ YOLOv8 (Object Detection)  
→ Bounding Boxes + Confidence Scores  

Key Design Decision:  
No intermediate CPU transfers. Tensor flow remains entirely within GPU memory during training and inference.

---

## Dataset

- **Dataset Used:** NTLNP  
- **Resolution:** 640 × 640  
- Optimized for nighttime wildlife scenarios  

---

## Performance Metrics

| Metric        | Score  |
|--------------|--------|
| Precision    | 0.974  |
| Recall       | 0.955  |
| mAP@0.5      | 0.976  |

Additional Evaluation:
- Loss convergence analysis  
- Training stability tracking  
- Detection confidence distribution analysis  
- Throughput benchmarking  

---

## Technical Stack
  
- YOLOv8 (Ultralytics)  
- Zero-DCE++  
