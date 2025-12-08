from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):

    prediction: float = Field(..., description="Prediction of the model", example=2.0)