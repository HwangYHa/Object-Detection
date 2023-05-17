from ultralytics import YOLO
import cv2

# Ultralytics YOLOv8의 최첨단 Yolo(You Only Look Once) 객체 감지 모델(실시간 개체 감지, 분류 및 분할)
model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Images/1.png", show=True) # model(str, Path) 로드하거나 생성할 모델 파일의 경로입니다.
cv2.waitKey(0)
