from chatterbot import ChatBot
import json
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Allaachiir")

with open('message_1.json') as f:
    d = json.load(f)
    conversations = []
    for element in d['messages']:
        try:
            print(element["content"])
            conversations.append(element["content"])
        except KeyError:
            pass


trainer = ListTrainer(chatbot)

trainer.train(conversations)
response = chatbot.get_response("Ah ok !")
print(response)