import requests

# Define the claim
data = {"claim": "NASA landed on the Moon in 1969"}

# Try both localhost and 127.0.0.1
try:
    response = requests.post("http://localhost:8000/fact-check", json=data)
except requests.exceptions.ConnectionError:
    response = requests.post("http://127.0.0.1:8000/fact-check", json=data)

# Print output
print("Status Code:", response.status_code)
print("Response:", response.json())
