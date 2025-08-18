import logging, inspect,datetime



def customLogger():
    
    # This is used to get the name of the calling function/class/method for where custom logging method Call.
    # Get the name of the calling function
    # This is useful for identifying which part of the code is generating the log messages
    # It uses inspect to get the stack frame and retrieves the function name from it
    
    logName = inspect.stack()[1][3]  # Get the name of the calling function
    
    # 2> Create a logger object with the name of the calling function
        # This allows you to have different loggers for different parts of your application
        # Each logger can have its own configuration and can be used independently
    logger = logging.getLogger(logName)
    
    # 3> Set the logging level to DEBUG
    logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG to capture all levels of logs
    
    # 4> Create a file handler to write logs to a file
    file_handler = logging.FileHandler('Python_Logging/CustomLogs.txt'.format(logName)) # Log file name with function name
    
    file_handler.setLevel(logging.DEBUG)  # Set the file handler logging level to DEBUG
    
    # 5> Create a formatter to define the format of the log messages
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p %A')
    
    # 6> Set the formatter for the file handler
    file_handler.setFormatter(formatter)
    
    # 7> Add the file handler to the logger
    logger.addHandler(file_handler)
    
    # 8>Finally Return the logger object
    return logger