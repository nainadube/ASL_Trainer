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