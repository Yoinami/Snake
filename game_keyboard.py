from pynput import keyboard


class game_Key_Board:
    
    def on_press(self, key):
        try:
            self.snake.pointing = key.char
        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        
    def __init__(self, snake) -> None:
        self.snake = snake
        l = keyboard.Listener(
            on_press=self.on_press, 
            on_release=self.on_release
            )
        l.start()
