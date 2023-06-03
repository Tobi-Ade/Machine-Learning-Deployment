import requests, json

url = "http://127.0.0.1:5000/result"

data = {
        "Product":"Credit card",
        "Issue":"Disclosure verification of debt",
        "Consumer_consent_provided": "Consent not provided",
        "Submitted_via":"Email",
        "Company_response_to_consumer":"Untimely response",
        "Timely_response":"No",
        "Year": "2017" 
       }

result = requests.post(url, json=data).json()

print(result)