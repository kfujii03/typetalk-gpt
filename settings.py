import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TYPETALK_TOKEN = os.environ.get('TYPETALK_TOKEN')
TYPETALK_TOPIC_ID = os.environ.get('TYPETALK_TOPIC_ID')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')