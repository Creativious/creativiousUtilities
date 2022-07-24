import json
import os

class MessageHandler:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.messages = {}
        if os.path.isfile(filepath):
            self.loadMessages()
    def getMessages(self):
        return self.messages
    def saveMessages(self, messages: dict):
        with open(self.__filepath, "w+") as f:
            f.write(json.dumps(self.messages))
    def loadMessages(self):
        with open(self.__filepath, "r") as f:
            self.messages = json.loads(f.read())