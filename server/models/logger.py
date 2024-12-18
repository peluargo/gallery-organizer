from datetime import datetime
from server.models.log_message_type import LogMessageType
from server.models.log_level import LogLevel
from server.models.log_message import LogMessage
from server.models.directory_manager import DirectoryManager

class Logger:
    def __init__(self,
                 class_name: str,
                 level: LogLevel = LogLevel.BASIC,
                 store_logs_in_file: bool = False,
                 log_file_prefix: str = 'log', 
                 log_file_directory: str = './logs',
                 directory_manager: DirectoryManager = None):
        self._class_name = class_name
        self._level = level
        self._store_logs_in_file = store_logs_in_file
        self._log_file_prefix = log_file_prefix
        self._log_file_directory = log_file_directory
        self._log_file_manager = directory_manager
        self._log_file_path = f'{self._log_file_directory}/{self._log_file_prefix}_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
        self._create_new_log_file() if store_logs_in_file else None

    def _create_new_log_file(self):
        self._log_file_manager.create_file(self._log_file_path)

    def _log_message_in_console(self, log_message: LogMessage):
        if log_message.get_type().value in self._level.value:
            print(str(log_message))

    def _log_message_in_file(self, log_message):
        self._log_file_manager.append_in_file(self._log_file_path, str(log_message))

    def _create_new_log_message(self, type, message):
        return LogMessage(self._class_name, message, type)
    
    def _log(self, type, message):
        log_message: LogMessage = self._create_new_log_message(type, message)
        self._log_message_in_console(log_message)
        self._log_message_in_file(log_message) if self._store_logs_in_file else None

    def info(self, message):
        self._log(LogMessageType.INFO, message)

    def warn(self, message):
        self._log(LogMessageType.WARN, message)

    def error(self, message):
        self._log(LogMessageType.ERROR, message)

    def debug(self, message):
        self._log(LogMessageType.DEBUG, message)