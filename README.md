# NutriDetect: AI-Powered Food Analysis for Diabetes Management 🍞🍕
**"Empowering diabetes patients with intelligent nutritional insights"**
<div>
  <img src="/images_app/app2.png" alt="NutriDetect" />
</div>
<!-- <div>
  <img src="/images_app/app.png" alt="NutriDetect" />
</div> -->

> A Sync AI Inc. Research Initiative for Advanced Diabetes Care

---
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-NutriDetect-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/Thirupathi986/Nutridetect)

---

![GitHub Repo stars](https://img.shields.io/github/stars/Thirupathi-Kadari/Nutridetect?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Thirupathi-Kadari/Nutridetect?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Thirupathi-Kadari/Nutridetect)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Thirupathi-Kadari/Nutridetect)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Contributors](https://img.shields.io/github/contributors/Thirupathi-Kadari/NutriDetect)

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Healthcare Impact](#-healthcare-impact)
3. [Key Features](#-key-features)
4. [Research Team](#-research-team)
5. [Technical Architecture](#-technical-architecture)
   - [Model Details](#model-details)
   - [Application Features](#application-features)
6. [Performance Metrics](#-performance-metrics)
7. [Dataset](#-dataset)
8. [Clinical Applications](#-clinical-applications)
9. [Application Screenshots](#-application-screenshots)
10. [Future Integration](#-future-integration)
11. [Hugging Face Space](#-hugging-face-space)
12. [Contributing](#-contributing)
13. [Contact](#-contact)
14. [License](#-license)

## 🍴 Overview
NutriDetect is a pioneering research project by Sync AI Inc., designed to enhance our remote health monitoring platform for diabetes patients. This advanced food recognition system will be integrated into our existing healthcare application, enabling patients to make informed dietary decisions through their smartphone cameras.

## 🏥 Healthcare Impact
- **Target Users**: Diabetes patients using Sync AI's remote monitoring platform
- **Clinical Value**: Real-time nutritional guidance for glucose management
- **Healthcare Integration**: Seamless incorporation with existing patient monitoring systems
- **Accessibility**: Mobile-first design for everyday meal decisions
- **Patient Empowerment**: Instant feedback on food choices and their potential impact on glucose levels

## 🔬 Key Features
- ✅ **Smart Food Analysis**: Advanced detection system using [YOLO](https://docs.ultralytics.com/) technology
- ✅ **Health-Focused Insights**: Nutritional analysis tailored for diabetes management
- ✅ **Clinical Integration**: Connects with Sync AI's healthcare monitoring platform
- ✅ **Real-time Recommendations**: Instant guidance on food choices
- ✅ **Future LLM Integration**: Planned multimodal capabilities for comprehensive health insights

## 👥 Research Team at Sync AI Inc.
- **Thirupathi Kadari** - Research Lead, AI Development
- **Syed Raheel Hussain** - Research Contributor, Healthcare Integration
- **Tushar Sinha** - Technical Advisor, Product Strategy

## 🛠 Technical Architecture

### Model Details
- **Vision Models**: YOLOv8m, YOLO11m
- **Framework**: [PyTorch](https://pytorch.org/)
- **Dataset**: Enhanced [UECFOOD dataset](https://drive.google.com/drive/folders/14rJclN97hZqe6bmGkTjnvPaDBBIF4v5w) with diabetes-relevant annotations
- **Deployment**: Healthcare-grade cloud infrastructure with mobile optimization

### Application Features
1. Real-time food detection and nutritional analysis
2. Glucose impact prediction capabilities
3. Integration with patient health records
4. HIPAA-compliant data handling
5. Future multimodal LLM integration

## 📊 Performance Metrics

| Model    | Image Size | Epochs | **mAP@0.5** | **mAP@0.5:0.95** |
|----------|------------|--------|-------------|------------------|
| YOLOv8m  | 640x640   | 26     | 🟢 0.652    | 🟠 0.507         |
| YOLO11m  | 640x640   | 48     | 🟢 0.758    | 🟠 0.601         |

## 🍽 Dataset
Current training utilizes an enhanced version of the UECFOOD dataset, augmented with diabetes-relevant nutritional information:
- [Base Dataset](https://drive.google.com/drive/folders/14rJclN97hZqe6bmGkTjnvPaDBBIF4v5w)

## 🩺 Clinical Applications
- **Glucose Management**: Real-time nutritional insights for better glucose control
- **Dietary Tracking**: Automated food logging and nutritional analysis
- **Healthcare Provider Integration**: Sharing detailed dietary data with medical teams
- **Personalized Recommendations**: AI-driven suggestions based on patient health patterns

## Application Screenshots
<div>
  <img src="/images_app/appscreen11.png" alt="NutriDetect-appscreen1" />
</div>
<div>
  <img src="/images_app/appscreen2.png" alt="NutriDetect-appscreen2" />
</div>

## 🔗 Future Integration
NutriDetect is being developed for seamless integration with Sync AI's diabetes management platform:
1. Integration with patient glucose monitoring systems
2. Multimodal LLM capabilities for comprehensive health insights
3. Advanced pattern recognition for personalized recommendations
4. Extended healthcare provider features

## 🤗 Hugging Face Space
[Hugging Face section remains the same...]

## 🤝 Contributing
[Contributing section remains the same...]

## 📫 Contact
For research collaboration or healthcare integration inquiries:
- 📧 **Thirupathi Kadari**: [Email](mailto:thirupathi.kadari986@gmail.com)
- 📧 **Sayed Raheel Hussain**: [Email](mailto:Sayedraheel1995@gmail.com)
- 📧 **Tushar Sinha**: [Email](mailto:tsr@justsync.ai)

## 📃 License
Copyright © 2024 Sync AI Inc. All rights reserved.

---
<p align="center">
Developed by Sync AI Inc. for advancing diabetes care through intelligent nutrition monitoring
</p>
