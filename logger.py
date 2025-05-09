from functools import wraps
import os
from config import Config
import logging

class Logger:
    def __init__(self, filename="mcp_server.log"):
        config = Config()
        logs_dir = config.get_logs_dir()
        
        # Create logs directory if it doesn't exist
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir, exist_ok=True)
            
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.FileHandler(logs_dir + "/" + filename))
        self.logger.addHandler(logging.StreamHandler())

    def read_log_file(self) -> str:
        with open(self.logger.pathName, "r") as file:
            return file.read()

    def info(self, message: str):
        self.logger.info(message)
        self.logger.flush()

    def error(self, message: str):
        self.logger.error(message)
        self.logger.flush()

    def warning(self, message: str):
        self.logger.warning(message)
        self.logger.flush()

    def debug(self, message: str):
        self.logger.debug(message)
        self.logger.flush()

    def exception(self, message: str):
        self.logger.exception(message)
        self.logger.flush()
