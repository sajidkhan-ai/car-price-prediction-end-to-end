import pandas as pd
import pickle

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    prediction = float(model.predict(df)[0])

    return {"prediction": prediction}