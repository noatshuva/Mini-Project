# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncore
from emailServer import emailServer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server = emailServer(('127.0.0.1', 30000), None)
    asyncore.loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
