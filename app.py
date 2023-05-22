## I want to build a python flask app that chats with GPT4ALL to generate bedtime stories based on user input.
## I want to use the GPT4ALL API to generate bedtime stories based on user input.
from flask import Flask, jsonify , request, render_template
import logging
from gpt4all_api import gpt4all_api_blueprint


app = Flask(__name__)

# Configure logging in app.py
def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

# Enable debug mode.
app.config["DEBUG"] = True

# Register the gpt4all_api blueprint
app.register_blueprint(gpt4all_api_blueprint)

# Configure logging
configure_logging()

# Landing page for the API
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    # return "<h1>GPT4ALL</h1><p>This site is a prototype API for GPT4ALL.</p>"


app.run( host='0.0.0.0', port=5001 )
