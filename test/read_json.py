import json

with open('message_1.json') as f:
    d = json.load(f)
    conversations = []
    for element in d['messages']:
        try:
            print(element["content"])
            conversations.append(element["content"])
        except KeyError:
            pass
    print(conversations)