from pynput import keyboard

def on_press(key):
    try:
        print(f'alphanumeric key {key.char} pressed')
        print(type(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
l = keyboard.Listener(
    on_press=on_press, 
    on_release=on_release
    )
l.start()

while True:
    pass