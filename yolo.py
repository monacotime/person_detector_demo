import torch, cv2

class YOLOv5:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        pass
    
    def run(self, img, stroke = 2):
        self.results = self.model(img).xyxy[0]
        image = img
        for result in self.results:
            image = cv2.rectangle(image, (result[0], result[1]), (result[2], result[3]), (255,255,255), stroke)
        return image