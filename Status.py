from enum import Enum

class Status(str, Enum):
    NOT_STARTED = 'NOT_STARTED'
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    ABORTED = 'ABORTED'