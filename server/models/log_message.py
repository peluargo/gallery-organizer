from datetime import datetime
from server.models.log_message_type import LogMessageType

class LogMessage:
    def __init__(self, 
                 class_name: str,
                 message: str, 
                 type: LogMessageType = LogMessageType.INFO):
        self._class_name = class_name
        self._message = message
        self._type = type
        self._timestamp: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def __str__(self):
        return f'[{self._timestamp}][{self._class_name}][{self._type.value}]: {self._message}'
    
    def get_message(self):
        return self._message

    def get_type(self):
        return self._type

    def get_timestamp(self):
        return self._timestamp