from PIL import Image

from ultralytics import YOLO

model = YOLO("yolo11n.pt")

# Train the model with MPS
results = model.train(data="data.yaml", epochs=1, imgsz=640, device="mps")
model.export()

