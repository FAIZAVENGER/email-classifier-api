import requests

url = "https://Fa12an-email-classifier-api.hf.space/classify"
payload = {
    "input_email_body": "Hi, my name is Aisha. My Aadhaar is 1234-5678-9123, my card number is 4111 1111 1111 1111, and my CVV is 321. Please help."
}
response = requests.post(url, json=payload)
print(response.json())

