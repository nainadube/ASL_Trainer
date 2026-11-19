from fastapi import FastAPI

app = FastAPI(
    title="ASL Trainer API",
    description="API for American Sign Language recognition",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ASL Trainer API!"
    }

from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = FastAPI(
    title="ASL Trainer API",
    description="API for American Sign Language recognition",
    version="1.0"
)

# Load trained model
model = load_model("models/asl_model.keras")


@app.get("/")
def home():
    return {"message": "Welcome to ASL Trainer API!"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("L")

    # Resize image
    image = image.resize((28, 28))

    # Convert image to numpy array
    image_array = np.array(image)

    # Normalize pixels
    image_array = image_array / 255.0

    # Reshape image
    image_array = image_array.reshape(1, 28, 28, 1)

    # Make prediction
    prediction = model.predict(image_array)

    # Get predicted class
    predicted_class = int(np.argmax(prediction))

    # Get confidence
    confidence = float(np.max(prediction))

    letters = "ABCDEFGHIKLMNOPQRSTUVWXY"

    predicted_letter = letters[predicted_class]

    return {
    "predicted_class": predicted_class,
    "predicted_letter": predicted_letter,
    "confidence": confidence
}