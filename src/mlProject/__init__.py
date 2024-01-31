import os
import sys
import logging


#logging message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#make logs directory
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        #stores logs into files using file handler
        logging.FileHandler(log_filepath),
        #prints logs on terminal
        logging.StreamHandler(sys.stdout)
    ]
)

#creating object
logger = logging.getLogger("mlProjectLogger")