# NutriDetect – AI Nutrition Companion, Simplifying One Meal at a Time 🍽️
**Empowering Health Seekers with Real-Time, AI-Driven Nutritional Analysis**

<div>
  <img src="/images_app/app1.png" alt="NutriDetect" />
</div>

> A Sync AI Inc. Research Initiative for Advancing Digital Healthcare

---
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-NutriDetect-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/JustSyncAI/NutriDetect)

---

![GitHub Repo stars](https://img.shields.io/github/stars/Thirupathi-Kadari/Nutridetect?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Thirupathi-Kadari/Nutridetect?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Thirupathi-Kadari/Nutridetect)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Thirupathi-Kadari/Nutridetect)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Contributors](https://img.shields.io/github/contributors/Thirupathi-Kadari/NutriDetect)

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Technical Contributions](#-technical-contributions)
3. [Architecture & Models](#-architecture--models)
4. [Dataset Details](#-dataset-details)
5. [Training Setup](#-training-setup)
6. [Evaluation Metrics](#-evaluation-metrics)
7. [Results & Insights](#-results--insights)
8. [Screenshots](#-screenshots)
9. [Future Directions](#-future-directions)
10. [Try on Hugging Face](#-try-on-hugging-face)
11. [Citation](#-citation)
12. [Contact](#-contact)
13. [License](#-license)

## 🍴 Overview
NutriDetect is an AI-powered food recognition system developed by Sync AI Inc. It uses deep learning models like YOLOv8 and Faster R-CNN to identify food items from images and estimate nutritional content. Designed to empower users—including those managing diabetes—it helps track daily meals, calorie intake, and dietary habits in real-time.

## ⚙️ Technical Contributions
- Combined UECFOOD256, Open Images, and other datasets to form 55,000+ annotated food images across 345 categories
- Trained two models:
  - YOLOv8 (real-time, mobile-ready)
  - Faster R-CNN (high-precision for clinical settings)
- Standardized annotation to YOLO format
- Built data augmentation pipeline and evaluation metrics framework

## 🧠 Architecture & Models
### 🔸 YOLOv8 (Ultralytics)
- Input: 640x640 images
- Epochs: 50
- Precision: 72.4%, Recall: 69.5%
- mAP@0.5: 75.9%, mAP@0.5:0.95: 60.1%

### 🔸 Faster R-CNN (Detectron2)
- Trained on GCP using NVIDIA L4 GPU
- Iterations: 100,000
- Precision: 68.5%, Recall: 66.3%
- mAP@0.5: 70.2%, mAP@0.5:0.95: 65.2%

## 🍽 Dataset Details
We used and combined:
- [UECFOOD256](https://www.kaggle.com/datasets/rkuo2000/uecfood256)
- Food subsets from [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)
- [School Lunch Dataset](https://drive.google.com/drive/folders/14rJclN97hZqe6bmGkTjnvPaDBBIF4v5w)
- Vietnamese food images (Pho, Banh Mi, etc.)

> All datasets were resized to 640x640, augmented (flips, rotations, color jitter), and converted to YOLO format.

## ⚙️ Training Setup
| Model        | Framework     | Batch Size | Duration   |
|--------------|---------------|------------|------------|
| YOLOv8       | Ultralytics   | 16         | 46 hours   |
| Faster R-CNN | Detectron2    | 8          | 37 hours   |

## 📊 Evaluation Metrics
- **Precision**: Correct positive predictions / Total positive predictions
- **Recall**: Correct positive predictions / All actual positives
- **mAP@0.5**: Average Precision @ IoU 0.5
- **mAP@0.5–0.95**: Mean AP over 10 IoU thresholds

## 📈 Results & Insights
| Model        | Precision | Recall | mAP@0.5 | mAP@0.5–0.95 |
|--------------|-----------|--------|---------|--------------|
| YOLOv8       | 72.4%     | 69.5%  | 75.9%   | 60.1%        |
| Faster R-CNN | 68.5%     | 66.3%  | 70.2%   | 65.2%        |

- YOLOv8: Better for mobile and fast inference
- Faster R-CNN: Better for small objects, occlusion, clinical use

## 🖼️ Screenshots
<div>
  <img src="/images_app/appscreen11.png" alt="NutriDetect Screenshot 1" />
</div>
<div>
  <img src="/images_app/appscreen2.png" alt="NutriDetect Screenshot 2" />
</div>

## 🚀 Future Directions
- Augmented reality integration for real-time food feedback
- Wearable device data fusion (e.g., glucose monitors)
- Multimodal models for full meal context understanding

## 🤗 Try on Hugging Face
Visit [Hugging Face NutriDetect Space](https://huggingface.co/spaces/JustSyncAI/NutriDetect) to:
- Upload food photos
- View detected items & nutritional insights

## 📖 Citation
```
@article{NutriDetect2025,
  title={NutriDetect – AI-powered food recognition and nutritional tracking system},
  author={Thirupathi Kadari, Kanchan Maurya, Tushar Sinha},
  journal={Sync AI Inc. Research},
  year={2025},
  url={https://github.com/sync-ai-inc/NutriDetect-x-SyncResearch}
}
```

## 📫 Contact
- 📧 **Thirupathi Kadari**: [thirupathi.kadari986@gmail.com](mailto:thirupathi.kadari986@gmail.com)
- 📧 **Kanchan Maurya**: [kanchan@justsync.ai](mailto:kanchan@justsync.ai)
- 📧 **Tushar Sinha**: [tsr@justsync.ai](mailto:tsr@justsync.ai)

## 📃 License
MIT License — see the [LICENSE](./LICENSE) file for details.

---
<p align="center">
Developed by Sync AI Inc. — Bridging AI, Nutrition, and Healthcare.
</p>
