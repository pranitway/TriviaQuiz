import requests

class Request_question():
    def __init__(self):
        self.parameters = {
            "amount" : 10,
            "type" : 'boolean',
            }
        self.question_data = self.fetch_questions()
        
    def fetch_questions(self):
        try:
            response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=self.parameters)
        except Exception as e:
            print("First connect to the internet...")
        else:
            response.raise_for_status()
            response.encoding = "utf-8"
            question_data = response.json()["results"]
            return question_data
