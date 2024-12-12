import sys

class Logger:
    def __init__(self, console = sys.stdout):
        self.console = console

    def log(self, message):
        self.console.write(str(message) + '\n')

    def up(self, lines = 1):
        self.console.write(f'\x1b[{lines}A')

    def clear(self):
        self.console.write('\x1b[2K')

    def clear_last_lines(self, lines = 1):
        for i in range(lines):
            self.up()
            self.clear()