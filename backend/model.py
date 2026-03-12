from ultralytics import YOLO
import uuid

model = YOLO("best.pt")

def run_inference(image_path):

    results = model(image_path)

    detections = []

    if results[0].boxes is not None:

        for box in results[0].boxes:

            class_id = int(box.cls[0])
            conf = float(box.conf[0])

            label = model.names[class_id]

            detections.append({
                "class": label,
                "confidence": round(conf,3)
            })

    output_image = "uploads/" + str(uuid.uuid4()) + ".jpg"

    annotated = results[0].plot()

    import cv2
    cv2.imwrite(output_image, annotated)

    return detections, output_image