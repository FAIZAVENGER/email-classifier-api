from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
from pii_masking import mask_text

app = FastAPI()

class EmailBody(BaseModel):
    input_email_body: str

model = joblib.load("email_classifier_model.pkl")

@app.post("/classify")
async def classify_email(body: EmailBody):
    input_email = body.input_email_body
    masked_email, entities = mask_text(input_email)
    category = model.predict([masked_email])[0]

    return {
        "input_email_body": input_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
