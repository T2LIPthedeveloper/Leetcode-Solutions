import requests

url = "https://apply-to-avantos.dev-sandbox.workload.avantos-ai.net"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
payload = {"email": "atul.parida@outlook.com"}  # Replace with your email

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.text)