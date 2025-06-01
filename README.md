# Email Classification API with PII Masking

## Overview
This project masks PII data in emails, classifies the email into support categories, and exposes it via a FastAPI endpoint.

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. Train the model:
```
python model_training.py
```

3. Run the API:
```
uvicorn api:app --reload
```

## API Endpoint

- **POST** `/classify`
- **Body**:
```json
{
  "input_email_body": "Your email text here"
}
```
- **Response**:
```json
{
  "input_email_body": "...",
  "list_of_masked_entities": [...],
  "masked_email": "...",
  "category_of_the_email": "..."
}
```
