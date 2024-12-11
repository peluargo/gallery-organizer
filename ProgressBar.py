import os
import sys
import math

class ProgressBar():
    def __init__(self, progress = 0, total = 100, fill = '░', empty = ' ', left_handle = '▌', right_handle = '▐'):
        self.progress = progress
        self.progress_percentage = 0
        self.total = total
        self.fill = fill
        self.empty = empty
        self.left_handle = left_handle
        self.right_handle = right_handle
        self.bar = None

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
        sys.stdout.write('\033[2A')
        print(f'Progress: {self.progress} / {self.total} ({self.progress_percentage}%)')
        print(self.bar)