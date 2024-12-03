# 🍔🍟 NutriDetect: Food Detection and Nutritional Insights 🍞🍕
**"Your gateway to smarter food recognition and health insights!"**

<div>
  <img src="/Images/NutriDetect.png" alt="NutriDetect" />
</div>

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
2. [Key Features](#-key-features)
3. [Research Team](#-research-team)
4. [Technical Architecture](#-technical-architecture)
   - [Model Details](#model-details)
   - [Application Features](#application-features)
5. [Performance Metrics](#-performance-metrics)
6. [Dataset](#-dataset)
7. [Why NutriDetect?](#-why-nutridetect)
8. [Application Screenshots](#-application-screenshots)
9. [Next Steps](#-next-steps)
10. [Hugging Face Space](#-hugging-face-space)
11. [Contributing](#-contributing)
12. [Contact](#-contact)
13. [License](#-license)

## 🍴 Overview
NutriDetect is an advanced platform designed to detect and classify food items from diverse cuisines. It's live on [Hugging Face](https://huggingface.co/spaces/Thirupathi986/Nutridetect), offering real-time object detection, classification, and nutritional insights.

## 🔬 Key Features
- ✅ **Diverse Dataset**: Images from global cuisines and restaurant chains.
- ✅ **State-of-the-Art Models**: Leveraging [YOLO](https://docs.ultralytics.com/) for precision and speed.
- ✅ **User-Centric Design**: Mobile and web-friendly for real-time detection.
- ✅ **Nutrition Insights**: Accurate nutritional content for detected items.
- ✅ **Interactive Demo**: Try NutriDetect live on [Hugging Face](https://huggingface.co/spaces/Thirupathi986/Nutridetect).

## 👥 Research Team
- **Thirupathi Kadari** - Project Lead
- **Syed Raheel Hussain** - Research Contributor
- **Tushar Sinha** - Visionary and Advisor

## 🛠 Technical Architecture

### Model Details
- **Models**: YOLOv8m, YOLO11m
- **Framework**: [PyTorch](https://pytorch.org/)
- **Dataset**: [UECFOOD dataset](https://drive.google.com/drive/folders/14rJclN97hZqe6bmGkTjnvPaDBBIF4v5w) with labeled bounding boxes for over 250+ food categories
- **Deployment**: Cloud-optimized and mobile-compatible

### Application Features
1. Multi-class object detection and classification
2. Bounding box generation with confidence scores
3. Real-time prediction capability
4. API-ready for easy integration with other platforms

## 📊 Performance Metrics

| Model    | Image Size | Epochs | **mAP@0.5** | **mAP@0.5:0.95** |
|----------|------------|--------|-------------|------------------|
| YOLOv8m  | 640x640   | 26     | 🟢 0.652    | 🟠 0.507         |
| YOLO11m  | 640x640   | 48     | 🟢 0.758    | 🟠 0.601         |

## 🍽 Dataset
You can find the dataset in the following locations:
- [Google Drive](https://drive.google.com/drive/folders/14rJclN97hZqe6bmGkTjnvPaDBBIF4v5w)

## 🤔 Why NutriDetect?
- 🌟 **Innovative Features**: Combines food detection with nutritional insights.
- 🌍 **Global Appeal**: Expanding to include a diverse range of cuisines.
- 💡 **Future-Oriented**: Plans to integrate with health apps and dietary tools.

## 📱 Application Screenshots

### Home Page
<div>
  <img src="./Images/Home_page.png" alt="Home Page">
</div>

### Description Page
<div>
  <img src="./Images/Description_page.png" alt="Description Page">
</div>

### Try Models Page
<div>
  <img src="./Images/Try_models.png" alt="Try Models Page">
</div>

### 🍔 Sample Results

**Single Food Detection:**
<div>
  <img src="./Images/Prediction_2.png" alt="Multiple Food Detection">
</div>

**Multiple Food Detection:**
<div>
  <img src="./Images/Prediction_1.png" alt="Single Food Detection">
</div>

### Nutritional Insights
**Detailed Nutritional Content Example:**
<div>
  <img src="./Images/Nutritional_content.png" alt="Nutritional Content">
</div>

## 🔗 Next Steps
NutriDetect aims to scale into a complete ecosystem with the following features:
1. Calorie tracking for dietary management
2. Recipe suggestions based on detected food items
3. Integration with health apps and devices

## 🤗 Hugging Face Space

NutriDetect is live on Hugging Face! Try out the application directly in your browser:

[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-NutriDetect-orange?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/Thirupathi986/Nutridetect)

Visit the Hugging Face Space to:
- Upload your food images and get real-time predictions.
- View bounding boxes and detailed nutritional insights.

Click the button above or [here](https://huggingface.co/spaces/Thirupathi986/Nutridetect) to explore!

## 🤝 Contributing
We welcome contributions! Here's how you can get involved:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## 📫 Contact
Have questions or want to collaborate? Reach out to us:
- 📧 **Thirupathi Kadari**: [Email](mailto:thirupathi.kadari986@gmail.com)
- 📧 **Sayed Raheel Hussain**: [Email](mailto:Sayedraheel1995@gmail.com)
- 📧 **Tushar Sinha**: [Email](mailto:tsr@justsync.ai)

## 📃 License
[License information to be added]
