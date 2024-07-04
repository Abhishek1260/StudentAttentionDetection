import cv2
from pathlib import Path
import uuid
import time

path = Path("images")

path.mkdir(exist_ok=True)

strs = [
    "Attention",
    "Not Attention(Not Seeing Screen)",
    "Not Attention(Sleeping)"
]

imgs = 50

cap = cv2.VideoCapture(0)
for category in strs:
    for i in range(imgs):
        print(f"Taking img for {category} img number {i}")
        rect , frame = cap.read()
        img = path / category
        img.mkdir(exist_ok = True)
        rand = uuid.uuid1()
        img_path = img / f"{category}-{rand}.jpg"
        cv2.imwrite(str(img_path) , frame)
        time.sleep(5)
    time.sleep(10)
