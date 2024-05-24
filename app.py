from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, request, jsonify, render_template
import yaml
import os

app = Flask(__name__)

def train_chatbot():
    chatbot = ChatBot(
        'ExtionInfotechBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )
    chatbot.storage.drop()
    with open('hw3.yaml', 'r') as file:
        data = yaml.safe_load(file)

    trainer = ListTrainer(chatbot)

    for category, conversations in data.items():
        for conversation in conversations:
            trainer.train(conversation)

    return chatbot

# Check if the database exists and remove it if it does
if os.path.exists('database.sqlite3'):
    os.remove('database.sqlite3')

chatbot = train_chatbot()

@app.route('/chat', methods=['POST'])
def chat():
  user_input = request.json.get('message')
  # Check if the user input is related to company
  if "company" in user_input.lower() or user_input.lower() == "c":
    # If there's a company category in YAML (optional)
    if "company" in data.keys(): 
      response = chatbot.get_response(random.choice(data["company"]))
    else:
      # If no company category, provide a default response
      response = chatbot.get_response("That's an interesting topic! I'm still learning about companies. Can you tell me more about what you're interested in?")
  else:
    # Use the existing logic for other inputs
    response = chatbot.get_response(user_input)
  return jsonify({'response': str(response)})

@app.route('/')
def home():
    return render_template('index.html')

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
