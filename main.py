from pynput.keyboard import *
import requests

is_released = True #prevents repeating calls

def on_press(key):
    global is_released
    if is_released: #if the is_released bool has been set back to true, basically if it isnt the 2nd pressed event in a row
        if key == KeyCode.from_char('w'):
            requests.get('http://10.0.0.213:5000/forwardUndef')
            print(f'pressed w: {key}')
        elif key == KeyCode.from_char('s'):
            requests.get('http://10.0.0.213:5000/backwardUndef')
            print(f'pressed s: {key}')
        elif key == KeyCode.from_char('a'):
            requests.get('http://10.0.0.213:5000/leftUndef')
            print(f'pressed a: {key}')
        elif key == KeyCode.from_char('d'):
            requests.get('http://10.0.0.213:5000/rightUndef')
            print(f'pressed d: {key}')
        else:
            print(f'invalid press: {key}')
        is_released = False

def on_release(key):
    global is_released
    is_released = True
    if key == KeyCode.from_char('w'):
        requests.get('http://10.0.0.213:5000/stop')
        print(f'released w: {key}')
    elif key == KeyCode.from_char('s'):
        requests.get('http://10.0.0.213:5000/stop')
        print(f'released s: {key}')
    elif key == KeyCode.from_char('a'):
        requests.get('http://10.0.0.213:5000/stop')
        print(f'released a: {key}')
    elif key == KeyCode.from_char('d'):
        requests.get('http://10.0.0.213:5000/stop')
        print(f'released d: {key}')
    elif key == Key.esc:
        # Stop listener
        return False
    else:
        print(f'invalid release: {key}')


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()