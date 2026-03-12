import os
import uuid
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from model import run_inference
from database import SessionLocal
from models import Detection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/")
def home():
    return {"message": "WildVision YOLO API running"}

# ... (keep your imports and setup the same)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    unique_name = str(uuid.uuid4()) + ".jpg"
    filepath = f"{UPLOAD_FOLDER}/{unique_name}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    detections, output_image = run_inference(filepath)

    db = SessionLocal()
    try:
        for d in detections:
            record = Detection(
                filename=unique_name,
                predicted_class=d["class"],
                confidence=d["confidence"],
                image_path=output_image
            )
            db.add(record)
        db.commit()
    finally:
        db.close() # CRITICAL: Close the connection to prevent DB locks

    return {
        "detections": detections,
        "image": "/" + output_image
    }


@app.get("/history")
def history():
    db = SessionLocal()
    try:
        # Fetch data and order by newest first
        data = db.query(Detection).order_by(Detection.id.desc()).all()
        
        # Convert SQLAlchemy objects to standard dictionaries so FastAPI can send it to Vue
        return [
            {
                "id": item.id, 
                "predicted_class": item.predicted_class, 
                "confidence": item.confidence
            } 
            for item in data
        ]
    finally:
        db.close() # CRITICAL: Close connection