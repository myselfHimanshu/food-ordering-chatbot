from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config

import json
import warnings
warnings.filterwarnings('ignore')


def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name="chat")


def run():
    interpreter = Interpreter.load("./models/nlu/default/chat")
    result = interpreter.parse(u"let's try some American food today")
    print(json.dumps(result, indent=2))


if __name__=="__main__":
    train_nlu("./data/nlu","./config.yml","./models/nlu")
    #run()
