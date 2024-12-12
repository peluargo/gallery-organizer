import os
import sys
import math
from Logger import Logger

class ProgressBar():
    def __init__(self, progress = 0, total = 100, fill = '░', empty = ' ', left_handle = '▌', right_handle = '▐', logger = Logger()):
        self.progress = progress
        self.progress_percentage = 0
        self.total = total
        self.fill = fill
        self.empty = empty
        self.left_handle = left_handle
        self.right_handle = right_handle
        self.bar = None
        self.logger = logger

    def update_progress_percentage(self):
        self.progress_percentage = math.ceil(100 * self.progress / self.total)

    def update_bar(self):
        bar = ''

        bar += self.left_handle 
        bar += self.fill * math.ceil(self.progress_percentage)
        bar += self.empty * math.ceil(100 - self.progress_percentage)
        bar += self.right_handle

        self.bar = bar

    def update(self):
        self.update_progress_percentage()
        self.update_bar()

    def increment(self, increment = 1):
        self.progress += increment
        self.update()

    def display(self):
        # give some top margin before printing the line
        self.logger.log('\n')

        # move console cursor up by two lines so that we can use
        # always the same line to print the progress bar, giving
        # it a smooth animation
        self.logger.clear_last_lines(2)
        self.logger.log(f'Progress: {self.progress} / {self.total} ({self.progress_percentage}%)')
        self.logger.log(self.bar)