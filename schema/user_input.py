from pydantic import BaseModel, Field, field_validator
from typing import Annotated

class UserInput(BaseModel):
    year: Annotated[int, Field(..., gt=0, description="Year on which car is manufactured", example=2002)]
    present_price: Annotated[float, Field(..., gt=0, description="Price of a car in lacs", example=2.2)]
    kms_driven: Annotated[int, Field(..., ge=0, description="kms driven by a car", example=2000)]

    # internal representation: integers expected by ML model
    fuel_type: Annotated[int, Field(..., description="0=Petrol,1=Diesel,2=CNG")]
    seller_type: Annotated[int, Field(..., description="0=Dealer,1=Individual")]
    transmission: Annotated[int, Field(..., description="0=Manual,1=Automatic")]
    owner: Annotated[int, Field(..., description="0=First Owner,1=Second Owner,3=Third Owner or Above")]

    @field_validator("fuel_type", mode="before")
    @classmethod
    def _fuel_type(cls, v):
        if isinstance(v, int):
            return v
        mapping = {"Petrol": 0, "Diesel": 1, "CNG": 2}
        try:
            return mapping[v]
        except Exception:
            raise ValueError("fuel_type must be one of: Petrol, Diesel, CNG")

    @field_validator("seller_type", mode="before")
    @classmethod
    def _seller_type(cls, v):
        if isinstance(v, int):
            return v
        mapping = {"Dealer": 0, "Individual": 1}
        try:
            return mapping[v]
        except Exception:
            raise ValueError("seller_type must be one of: Dealer, Individual")

    @field_validator("transmission", mode="before")
    @classmethod
    def _transmission(cls, v):
        if isinstance(v, int):
            return v
        mapping = {"Manual": 0, "Automatic": 1}
        try:
            return mapping[v]
        except Exception:
            raise ValueError("transmission must be one of: Manual, Automatic")

    @field_validator("owner", mode="before")
    @classmethod
    def _owner(cls, v):
        if isinstance(v, int):
            return v
        mapping = {"First Owner": 0, "Second Owner": 1, "Third Owner or Above": 3}
        try:
            return mapping[v]
        except Exception:
            raise ValueError("owner must be one of: First Owner, Second Owner, Third Owner or Above")