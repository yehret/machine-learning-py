import sys
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# --- ETUP PATHS & IMPORT MODEL ---
BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from src.model import SpaceClassifier

# --- INIT APP & LOAD MODEL ---
app = FastAPI()

templates = Jinja2Templates(directory="server/templates")

print("⏳ Loading AI Model...")
model_path = BASE_DIR / "models" / "space_model_v1.pkl"

classifier = SpaceClassifier()
classifier.load(model_path)
print("✅ Model Loaded Successfully!")

# --- DATA MODELS ---
class DescriptionRequest(BaseModel):
    text: str

# --- ROUTES ---
@app.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(item: DescriptionRequest):
    prediction = classifier.predict(item.text)
    
    return JSONResponse(content={"prediction": prediction})