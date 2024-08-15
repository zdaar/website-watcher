from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

template_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "templates")
)
app = Flask(__name__, template_folder=template_dir)

from app import routes
