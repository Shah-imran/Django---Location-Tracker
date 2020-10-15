from dotenv import load_dotenv
from pathlib import Path
import os

ENV_PATH = os.path.join(Path(__file__).resolve().parent.parent.parent, '.env')

load_dotenv(ENV_PATH)

DEBUG = False

ALLOWED_HOSTS = ["farhad.pythonanywhere.com"]
