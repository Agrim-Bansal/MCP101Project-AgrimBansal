import cv2
from PIL import Image

from ultralytics import YOLO

model = YOLO("yolo11n.pt")

# im1 = Image.open("bus.jpg")
# results = model.predict(source=im1, save=True)  # save plotted images


results = model("bus.jpg")

# Visualize the results
for result in results:
    result.show()