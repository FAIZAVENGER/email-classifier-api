---
# 📧 Email Classification & PII Masking API

A powerful FastAPI-based system that automatically classifies emails (e.g., as incidents or problems) and masks sensitive Personally Identifiable Information (PII) such as Aadhaar numbers, phone numbers, CVV, card numbers, and more.

🚀 **Live Demo:**
[Try it on Hugging Face Spaces](https://Fa12an-email-classifier-api.hf.space/classify)
---

## ✨ Features

- ✅ **PII Masking**: Detects and masks entities like Aadhaar, CVV, card numbers, phone numbers, etc.
- ✅ **Email Classification**: Categorizes emails into types (e.g., _Incident_, _Request_, _Complaint_) using an ML pipeline.
- ✅ **Deployed API**: Hosted on Hugging Face Spaces using FastAPI + Docker.
- ✅ **Model Compression**: Joblib-compressed `.pkl` for efficient inference and deployment.

---

## 🧠 Technologies Used

| Tool/Library | Purpose                          |
| ------------ | -------------------------------- |
| Python 3.9   | Core programming language        |
| FastAPI      | Web framework for API deployment |
| spaCy        | NLP and PII detection            |
| scikit-learn | Email classification model       |
| Uvicorn      | ASGI server                      |
| Hugging Face | Deployment of API                |
| Docker       | Custom container environment     |

---

## 📦 API Endpoint

**POST** `/classify`

**Payload Example:**

```json
{
  "input_email_body": "Hi, my name is Aisha. My Aadhaar is 1234-5678-9123 and CVV is 123."
}
```

````

**Response Example:**

```json
{
  "input_email_body": "Hi, my name is Aisha. My Aadhaar is 1234-5678-9123 and CVV is 123.",
  "list_of_masked_entities": [
    {
      "position": [37, 51],
      "classification": "aadhar_num",
      "entity": "1234-5678-9123"
    },
    {
      "position": [63, 66],
      "classification": "cvv_no",
      "entity": "123"
    }
  ],
  "masked_email": "Hi, my name is Aisha. My Aadhaar is [aadhar_num] and CVV is [cvv_no].",
  "category_of_the_email": "Incident"
}
```

---

## ⚠️ Model File Note

The trained model file `email_classifier_model.pkl` is **not included** in this repository due to [GitHub’s 100MB file limit](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

> 🧪 You can still use the model live via our [Hugging Face API deployment](https://Fa12an-email-classifier-api.hf.space/classify)

---

## 🛠️ Local Development (Optional)

Clone and run locally:

```bash
git clone https://github.com/FAIZAVENGER/email-classifier-api.git
cd email-classifier-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn api:app --reload
```

---

## 👤 Author

**Mohammed Faizan Khan**
Email: [mfaizankh007@gmail.com](mailto:mfaizankh007@gmail.com)
GitHub: [@FAIZAVENGER](https://github.com/FAIZAVENGER)

---



````
