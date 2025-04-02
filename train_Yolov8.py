# ======================================
#  YOLOv8 Training Script for NutriDetect
# ======================================

import os
import warnings
import zipfile
from google.cloud import storage
from ultralytics import YOLO

warnings.filterwarnings("ignore")

# ===========================
# Configuration for GCP Dataset
# ===========================
bucket_name = "thirupathi"
zip_blob_name = "UECFOOD256_Yolo_1.zip"
yaml_blob_name = "data.yaml"
destination_dir = "/home/jupyter/yolo_dataset"

os.makedirs(destination_dir, exist_ok=True)

# Initialize GCS client
client = storage.Client()
bucket = client.bucket(bucket_name)

# Download ZIP dataset from GCS
zip_blob = bucket.blob(zip_blob_name)
zip_path = os.path.join(destination_dir, zip_blob_name)
zip_blob.download_to_filename(zip_path)
print(f"✅ Downloaded dataset ZIP: {zip_blob_name}")

# Download YAML file
yaml_blob = bucket.blob(yaml_blob_name)
yaml_path = os.path.join(destination_dir, yaml_blob_name)
yaml_blob.download_to_filename(yaml_path)
print(f"✅ Downloaded data config: {yaml_blob_name}")

# Unzip the dataset
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(destination_dir)
    print("✅ Extracted dataset successfully.")

# ===========================
# Training the YOLOv8 Model
# ===========================
model = YOLO('yolov8m.pt')  # Load pre-trained YOLOv8m model

print("\n🚀 Starting training...")
model.train(
    data=os.path.join(destination_dir, 'data.yaml'),
    epochs=100,
    imgsz=640
)

# ===========================
# Evaluation on Validation Set
# ===========================
trained_model_path = 'runs/detect/train5/weights/best.pt'
model = YOLO(trained_model_path)

print("\n🔍 Running validation...")
metrics = model.val(
    data=os.path.join(destination_dir, 'data.yaml'),
    imgsz=640
)

# ===========================
# Display Metrics
# ===========================
print("\n📊 Evaluation Metrics:")
print(metrics)
