import requests

url = "http://127.0.0.1:8080/predict"
obj = [1.070,1.323,0.861,0.433,0.074,0.073]
x = requests.post(url, json=obj)

print(x.text)