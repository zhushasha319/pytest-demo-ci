import logging
import os 
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report", "logs")
os.makedirs(LOG_DIR, exist_ok=True)