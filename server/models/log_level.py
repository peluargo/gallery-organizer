from enum import Enum

class LogLevel(str, Enum):
    BASIC = ['INFO', 'WARN', 'ERROR']
    DEBUG = ['INFO', 'WARN', 'ERROR', 'DEBUG']