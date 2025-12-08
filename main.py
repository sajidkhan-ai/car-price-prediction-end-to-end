from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, MODEL_VERSION
from schema.prediction_response import PredictionResponse

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Car price prediction API"}

@app.get("/health")
def health():
    return {
        "status code": "OK",
        "Model Version": MODEL_VERSION
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserInput):
    input = {
        "Year": data.year,
        "Present_Price": data.present_price,
        "Kms_Driven": data.kms_driven,
        "Fuel_Type": data.fuel_type,
        "Seller_Type": data.seller_type,
        "Transmission": data.transmission,
        "Owner": data.owner
    }
    try:
        prediction = predict_output(input)
        return prediction
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))