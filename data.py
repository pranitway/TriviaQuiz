import requests

parameters = {
    "amount" : 10,
    "type" : 'boolean',
}

try:
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
except Exception as e:
    print("First connect to the internet...")
else:
    response.raise_for_status()
    response.encoding = "utf-8"
    question_data = response.json()["results"]
