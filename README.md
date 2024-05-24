# AI-chatbot
# Extion Infotech Chatbot

This is a chatbot project for Extion Infotech, built using Flask and ChatterBot. The chatbot is trained to respond to various questions related to Extion Infotech's services, mission, and general information.

## Project Structure
my_chatbot/
│
├── app.py
├── database.sqlite3
├── hw1.yaml
├── requirements.txt
└── templates/
└── index.html

## Files Description

- `app.py`: The main Flask application file that initializes and trains the chatbot, and sets up the API endpoints.
- `database.sqlite3`: The SQLite database file used by ChatterBot to store conversation data.
- `hw1.yaml`: The YAML file containing the training data for the chatbot.
- `requirements.txt`: A list of Python dependencies required for the project.
- `templates/index.html`: The HTML template for the chat interface.

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/my_chatbot.git
    cd my_chatbot
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv my_chatbot_env
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```bash
        my_chatbot_env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source my_chatbot_env/bin/activate
        ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask application:**

    ```bash
    python app.py
    ```

6. **Access the chat interface:**

    Open a web browser and go to `http://localhost:5000`.

## Training Data

The chatbot is trained using data provided in the `hw1.yaml` file. The file is structured as follows:

```yaml
greetings:
  - - Hi
    - Hello!
  - - How are you?
    - I am doing well, thank you!

smalltalk:
  - - What services does Extion Infotech offer?
    - Extion Infotech offers a range of services including software development, web design and development, mobile app development, digital marketing, e-commerce solutions, and consulting services.
  - - Can you tell me more about the software development services offered by Extion Infotech?
    - Certainly! Extion Infotech specializes in custom software development tailored to meet the unique needs of businesses across various industries.

farewells:
  - - Goodbye
    - Farewell!
  - - See you later
    - Have a great day!
