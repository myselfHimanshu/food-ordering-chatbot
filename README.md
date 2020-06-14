# Food Ordering and Help & Support Chatbot

Food Ordering Chatbot using RASA.

## Steps:

Clone the repo.

1. Install Anaconda3
2. Create Environment and install requirements and activate the environment
```bash
$conda create --name <env-name> --file requirements.txt
```

Main Bot file to run:
```
$python bot.py
```

**Some points about RASA**:

1. Requires installations of multiple components
2. Requires tech knowledge
3. Open-source
4. No interface needed, can write down in json or md format
5. Host the data or bot on our own server

## Building the conversational states

First let's define how our chatbot should converse like. Just a flow diagram.

![](https://github.com/myselfHimanshu/food-ordering-chatbot/raw/master/readme/1.png)

### 

## RASA core training


<p align="center">
  <img width="50%" height="50%" src="https://github.com/myselfHimanshu/food-ordering-chatbot/raw/master/readme/2.png"/>
</p>

1. **training_data**: these are the stories that define the normal converation.

   ```basic
   ## Generated Story -7329490837376575624
   * greetings.hello
       - utter_greetings.hello
       - utter_agent.welcome
       - utter_ask.cuisine
   * cuisine.type{"cuisine": "mexican"}
       - slot{"cuisine": "mexican"}
       - utter_display.menu
       - utter_select.item
   * confirm.affirm
       - utter_order.placed
   ```

2. **domains**: this defines the environment in which bot operates. It specifies `intents`,`entities`,`slots`,`actions` the bot should know about and `templates`for the things bot can say.

3. **load_agent**: bot is first loaded with some parameters to determine how the stories and other data can be converted into features for training the bot.

4. **policies**: this is one of the parameter in load_agent. The policy decides which action to take at every step in the conversation. Find more about policies [here](https://rasa.com/docs/core/policies/).
   **Note:** *tensorflow_embedding* pipeline can be used to assign two or more intents to a single input message.

5. **load_data**: you load the data using the stories training file and defined domain file.

6. **training**: policies work in ensemble, we can pass more than 1 policy, it will train separately and will be used together in ensemble for prediction.

7. **persist**: when model is trained, it is then persisted to some storage.

## Predictions

![](https://github.com/myselfHimanshu/food-ordering-chatbot/raw/master/readme/3.png)

1. **load model**: first task is to load the trained model.
2. **start_server**: we can user Flask.
3. **interpreter**: it's job is to classify the intent with entity extraction and these entities can be used as slots in the conversation.
4. **create_tracker**: this is created to track all the objects of a key say user_id. To make it easy to use slots of a particular user_id. RASA has inbuilt Memory Tracker. We can use MongoTrackerStore when scaling up.
5. **create_features**: create freatures of the objects present in tracker based on the policy
6. **policy_ensemble**: if we have more than one policy, each policy will output a score and max is taken to determine the next action
7. **update_tracker**: once the action is performed, we will update the tracker.
8. **bot_text**: the bot message to user (the action).

## Preparing and training the chatbot

The code is provide here : [github/food-ordering-chatbot](https://github.com/myselfHimanshu/food-ordering-chatbot)

## Other components that are required

- database for item availability
- storage to keep order until it's placed/confirmed.
- storage to keep user's data (id, name, phone-number, address, previous orders)
- payment gateway/wallet
- notifications : can be a genral notification or for some coupons/codes
- assigned person for delivery ( to update on chatbot) ( person_name, phone-number)

## TODO

- [ ] Flask web app

I will include basic flask application for chatting with the bot.
