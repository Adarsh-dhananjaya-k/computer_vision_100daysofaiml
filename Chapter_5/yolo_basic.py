from ultralytics import YOLO

model = YOLO('yolov8n.pt')
result = model('Chapter_5/images/img.png',show=True)
cv2.waitKey(0)