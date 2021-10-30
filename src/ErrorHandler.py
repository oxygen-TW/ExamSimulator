import logging
from logging.handlers import RotatingFileHandler
from getpass import getuser
from enum import Enum

class LogLevelNotValid(Exception):
    pass

class LogLevel(Enum):
    Debug=10
    Info=20
    Warning=30
    Error=40
    Critical=50

class EsLogger():
    def __init__(self, logLevel) -> None:
    
        #https://stackoverflow.com/questions/24505145/how-to-limit-log-file-size-in-python
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s (%(lineno)d) %(message)s')

        logFile = 'test.log' #Set to program file

        my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                        backupCount=1, encoding="utf-8", delay=0)
        my_handler.setFormatter(log_formatter)
        my_handler.setLevel(logLevel.value)

        self.app_log = logging.getLogger(getuser())
        self.app_log.setLevel(logLevel.value)

        self.app_log.addHandler(my_handler)

    def writeLog(self, errorLog, level: LogLevel):
        if(level.value == 10):
            self.app_log.debug(errorLog)
        elif(level.value == 20):
            self.app_log.info(errorLog)
        elif(level.value == 30):
            self.app_log.warning(errorLog)
        elif(level.value == 40):
            self.app_log.error(errorLog)
        elif(level.value == 50):
            self.app_log.critical(errorLog)
        else:
            self.app_log.error("Exception: LogLevelNotValid")
            raise LogLevelNotValid

if(__name__ == "__main__"):
    Es = EsLogger(LogLevel.Debug)
    Es.writeLog("123", LogLevel.Debug)