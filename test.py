import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 40, "name": "aisha", "views": 50000},
        {"likes": 78, "name": "How to make REST API", "views": 10000},
        {"likes": 100, "name": "Learn all about ARGS PARSER", "views": 70000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response  = requests.get(BASE + "video/2")
print(response.json())
