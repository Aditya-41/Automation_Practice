import logging,datetime

# from Python_Logging.customLogs import customLogger as cl
from customLogs import customLogger 
class CustomLogs:
    log = customLogger()  # Create a custom logger instance
    
    def method1(self):
        self.log.info('This is an info message from method1')
        self.log.warning('This is a warning message from method1')
        self.log.error('This is an error message from method1')
        self.log.critical('This is a critical message from method1')
        
    def method2(self):
        m2 = customLogger()  # Create another custom logger instance
        m2.info('This is an info message from method2')
        m2.warning('This is a warning message from method2')
        m2.error('This is an error message from method2')
        m2.critical('This is a critical message from method2')
        
        # self.log.info('This is an info message from method2')
        # self.log.warning('This is a warning message from method2')
        # self.log.error('This is an error message from method2')
        # self.log.critical('This is a critical message from method2')
    
    
cld = CustomLogs()  # Create an instance of CustomLogger
cld.method1()  # Call method1
cld.method2()  # Call method2