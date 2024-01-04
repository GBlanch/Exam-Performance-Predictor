import logging
import os
from datetime import datetime

# Create log directory
# Name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Path
logs_path = os.path\
              .join(os.getcwd(),
                   "logs",
                    LOG_FILE)
# Directory itself
os.makedirs(logs_path,
            exist_ok = True)

# Create log file path
LOG_FILE_PATH = os.path\
                .join(logs_path,
                      LOG_FILE)

# Alter the root logger
# https://machinelearningmastery.com/logging-in-python/#:~:text=The%20call%20to%20logging.,output%20to%20include%20the%20time.
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
