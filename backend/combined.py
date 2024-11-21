import os
import cv2
import numpy as np
import tensorflow as tf

from PIL import Image
from ultralytics import YOLO


class CombinedModels:
    def __init__(self, yolo_path, effnet_path):
        self.class_names = ['a', 'ba', 'ca', 'da', 'e', 'ee', 'eu', 
                            'fa', 'ga', 'ha', 'i', 'ja', 'ka', 'la', 
                            'ma', 'na', 'nga', 'nya', 'o', 'pa', 'qa', 
                            'ra', 'sa', 'ta', 'u', 'va', 'vowels_e', 
                            'vowels_ee', 'vowels_eu', 'vowels_h', 
                            'vowels_i', 'vowels_la', 'vowels_ng', 
                            'vowels_o', 'vowels_r', 'vowels_ra', 
                            'vowels_u', 'vowels_x', 'vowels_ya', 
                            'wa', 'xa', 'ya', 'za']
        
        self.yolo = YOLO(yolo_path)
        self.effnet = tf.keras.models.load_model(effnet_path)
    
    def process_image(self, image_path, yolo_conf=0.5):
        """
        Processing Image through YOLO and EfficientNetV2
        """

        if not os.path.exists(image_path):
            print(f'ERROR: Image not found at {image_path}')
            return None
        
        yolo_image = self.preprocess_for_yolo(image_path)
        results = self.yolo(yolo_image, conf=yolo_conf)

        detections = []
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            confidence = box.conf
            names = results[0].names[int(box.cls)]
            detections.append([
                x1.item(),
                y1.item(),
                x2.item(),
                y2.item(),
                confidence.item(),
                str(names)
            ])

        detections = self.sort_detections(detections)

        detected_labels = []
        # eff_labels = []
        # yol_labels =[]
        for _, (x1, y1, x2, y2, confidence, names) in enumerate(detections):
            cropped = yolo_image[int(float(y1)): int(float(y2)),
                                int(float(x1)): int(float(x2))]
            effnet_image = self.preprocess_for_effnet(cropped)
            effnet_image = np.expand_dims(effnet_image, axis=0)
            effnet_pred = self.effnet.predict(effnet_image, verbose=0)
            effnet_class = np.argmax(effnet_pred)
            effnet_conf = effnet_pred[0][effnet_class]
            effnet_names = self.get_class_name(int(effnet_class))

            if float(effnet_conf) > float(confidence):
                final_class = effnet_names
            else:
                final_class = names
            
            # eff_labels.append(effnet_names)
            # yol_labels.append(names)
            detected_labels.append(names)

        return self.arrange_words(detected_labels)
        # return self.arrange_words(detected_labels), self.arrange_words(eff_labels), self.arrange_words(yol_labels)
    
    def preprocess_for_yolo(self, image_path):
        image = Image.open(image_path)
        image = image.convert('RGB')
        image = np.array(image)
        yolo_input = cv2.resize(image, (640, 640), interpolation=cv2.INTER_LINEAR)

        return yolo_input
    
    def preprocess_for_effnet(self, image):
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_LINEAR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_array = np.array(image)
        image_array = np.stack((image_array,) * 3, axis=-1)
        image_array = image_array / 255.

        return image_array
    
    def sort_detections(self, detections):
        detections = np.array(detections)
        sorted_detections = sorted(detections, key=lambda x: float(x[0]))
        
        return sorted_detections
    
    def get_class_name(self, class_id):
        if 0 <= class_id < len(self.class_names):
            return self.class_names[class_id]
        return f"unknown_{class_id}"
    
    def arrange_words(self, labels):
        words = []
        
        for id, label in enumerate(labels):
            if label == 'vowels_ee':
                if id < len(labels) - 1:
                    labels[id + 1] = labels[id + 1].replace(list(labels[id + 1])[-1], 'é')
                continue
            
            if words:
                if label == 'vowels_e':
                    prev_word = words.pop()
                    label = prev_word.replace(list(prev_word)[-1], 'e')
                elif label == 'vowels_eu':
                    prev_word = words.pop()
                    label = prev_word.replace(list(prev_word)[-1], 'eu')
                elif label == 'vowels_i':
                    prev_word = words.pop()
                    label = prev_word.replace(list(prev_word)[-1], 'i')
                elif label == 'vowels_o':
                    if words[-1] == 'r' or words[-1] == 'ng':
                        words[-2] = str(words[-2]).replace(list(str(words[-2]))[-1], 'o')
                        label = ''
                    else:
                        prev_word = words.pop()
                        label = prev_word.replace(list(prev_word)[-1], 'o')
                elif label == 'vowels_u':
                    prev_word = words.pop()
                    label = prev_word.replace(list(prev_word)[-1], 'u')
                elif label == 'vowels_x':
                    prev_word = words.pop()
                    label = prev_word.replace(list(prev_word)[-1], '')
                elif label == 'vowels_h':
                    label = 'h'
                elif label == 'vowels_r':
                    label = 'r'
                elif label == 'vowels_ng':
                    label = 'ng'
                elif label == 'vowels_ra':
                    prev_word = words.pop()
                    label = ''.join((prev_word[0], 'r', prev_word[1:]))
                elif label == 'vowels_la':
                    prev_word = words.pop()
                    label = ''.join((prev_word[0], 'l', prev_word[1:]))
                elif label == 'vowels_ya':
                    prev_word = words.pop()
                    label = ''.join((prev_word[0], 'y', prev_word[1:]))

            words.append(label)

        return ''.join(word for word in words).lower()
