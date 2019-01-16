from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from rasa_core.agent import Agent

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# loading the nlu training samples
training_data = load_data("./data/nlu")

# trainer to educate our pipeline
trainer = Trainer(config.load("./config.yml"))

# train the model!
interpreter = trainer.train(training_data)

# store it for future use
model_directory = trainer.persist("./models/nlu", fixed_model_name="chat")

agent = Agent.load('models/dialogue', interpreter=model_directory)

print("Your bot is ready to talk! Type your messages here or send 'stop'")
print("\n\n")
print("Bot: ","Yo!!! Hey there....")
while True:

    a = input("User: ")
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        print("BOT: ",response["text"])
