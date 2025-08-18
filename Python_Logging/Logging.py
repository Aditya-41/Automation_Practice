import logging
import datetime


# Configure the logging
logging.basicConfig(
    filename='Python_Logging/logs.txt',  # Log file name
    level=logging.DEBUG,  # Set the logging level to DEBUG to capture all levels of logs
    format='%(asctime)s %(levelname)s: %(message)s',  # Format for the log messages
    datefmt='%d/%m/%Y %I:%M:%S %p %A'  # Custom date format
)
logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')
