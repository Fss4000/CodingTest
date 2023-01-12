import json


with open("./bread.json", encoding="UTF-8") as f:
    data = json.loads(f)
    print(data)
    print("")