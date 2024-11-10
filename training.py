from PIL import Image
from roboflow import Roboflow
from ultralytics import YOLO


model = YOLO("yolov9c.pt")
model = model.load("best.pt")
# Train the model with MPS
results = model.train(data="data.yaml", epochs=1)
model.export()
