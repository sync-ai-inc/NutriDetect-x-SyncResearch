import os
import logging
from detectron2.engine import DefaultTrainer
from detectron2.config import get_cfg
from detectron2.data.datasets import register_coco_instances
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data import DatasetMapper, build_detection_train_loader
from detectron2.utils.logger import setup_logger
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
from detectron2.data import detection_utils as utils
from detectron2.structures import BoxMode

# Initialize logger
setup_logger()

# === Dataset Paths ===
train_json = "/workspace/json_files/coco_annotations_train.json"
val_json = "/workspace/json_files/coco_annotations_val.json"
images_path = "/workspace/images"

# === Register COCO Format Datasets ===
register_coco_instances("food_train", {}, train_json, os.path.join(images_path, "train"))
register_coco_instances("food_val", {}, val_json, os.path.join(images_path, "val"))

# Verify dataset registration
print("Train Metadata:", MetadataCatalog.get("food_train"))
print("Val Metadata:", MetadataCatalog.get("food_val"))

# === Custom DatasetMapper to handle size mismatch errors ===
class CustomDatasetMapper(DatasetMapper):
    def __call__(self, dataset_dict):
        try:
            return super().__call__(dataset_dict)
        except utils.SizeMismatchError:
            logging.warning(f"Skipping image due to size mismatch: {dataset_dict['file_name']}")
            return None

# === Custom Trainer using Custom Mapper ===
class CustomTrainer(DefaultTrainer):
    @classmethod
    def build_train_loader(cls, cfg):
        return build_detection_train_loader(cfg, mapper=CustomDatasetMapper(cfg, is_train=True))

# === Configuration ===
cfg = get_cfg()
cfg.merge_from_file("configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
cfg.DATASETS.TRAIN = ("food_train",)
cfg.DATASETS.TEST = ("food_val",)
cfg.DATALOADER.NUM_WORKERS = 4
cfg.MODEL.WEIGHTS = "detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl"
cfg.SOLVER.IMS_PER_BATCH = 8
cfg.SOLVER.BASE_LR = 0.001
cfg.SOLVER.MAX_ITER = 100000
cfg.SOLVER.STEPS = (70000, 90000)
cfg.SOLVER.GAMMA = 0.1
cfg.SOLVER.CHECKPOINT_PERIOD = 5000
cfg.TEST.EVAL_PERIOD = 5000
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 345
cfg.OUTPUT_DIR = "./output"
os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)

# === Training ===
trainer = CustomTrainer(cfg)
trainer.resume_or_load(resume=False)
trainer.train()

# === Evaluation ===
evaluator = COCOEvaluator("food_val", cfg, False, output_dir=cfg.OUTPUT_DIR)
val_loader = build_detection_test_loader(cfg, "food_val")
print("\nEvaluating model on validation dataset...")
evaluation_results = inference_on_dataset(trainer.model, val_loader, evaluator)

# === Display Results ===
print("\nEvaluation Results:")
print(evaluation_results)
