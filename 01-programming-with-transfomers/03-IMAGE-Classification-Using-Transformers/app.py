# Install YOLOv5 dependencies
# pip install torch torchvision
from ultralytics import YOLO
import cv2

# Load a pre-trained YOLOv5 model (trained on COCO dataset)
model = YOLO("yolov5s.pt")  # 's' = small, fast version

# Load an image
image_path = "data/image1.png"  # replace with your image file
results = model(image_path)

# Show results
results[0].show()  # opens a window with detections

# Print detected objects
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        print(f"Detected: {label}")
