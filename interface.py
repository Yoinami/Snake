import random, sys, time
import game_keyboard, snake

class Game_core:
    def __init__(self) -> None:
        self.game_state = True
        self.GRID_X_Y = 20
        self.fruit = [random.randint(0,self.GRID_X_Y-1), random.randint(0,self.GRID_X_Y-1)]
        self.snake = snake.Snake()
        self.snake.location.append([5, self.GRID_X_Y//2])
        self.snake.add_snake()
        self.k = game_keyboard.game_Key_Board(self.snake)
        self.grid_array = [[x, y] for x in range(self.GRID_X_Y) for y in range(self.GRID_X_Y)]
    
    def print(self):
        """Main game loop"""

        #reset the game board
        print("\u001b[100D", end="")
        print("\u001b[100A", end="")
        sys.stdout.flush()
        time.sleep(0.5)

        #snake movement
        self.snake.move_snake()
        if self.snake.dies_from_self() or self._dies_from_box():
            self.game_state = False
        if self.snake._check_collision_with_apple(self.fruit[0], self.fruit[1]):
            self.rechoose_apple_position()

        #the main grid function
        for y in range(-1, self.GRID_X_Y + 1):
            for x in range(-1, self.GRID_X_Y + 1):
                if(x==-1 or y==-1 or x==self.GRID_X_Y or y==self.GRID_X_Y):
                    print("# ", end="")
                elif x == self.fruit[0] and y == self.fruit[1]:
                    print("o ", end="")
                elif self.snake.check_location([x, y]):
                    print("* ", end="")
                else:
                    print("  ", end="")
            print()

    def rechoose_apple_position(self):
        grid_copy = self.grid_array.copy()
        for i in self.grid_array:
            if self.snake.check_location(i):
                grid_copy.remove(i)
        self.fruit = random.choice(grid_copy)

    def _dies_from_box(self):
        if (self.snake.location[0][0] >= self.GRID_X_Y or 
            self.snake.location[0][0] < 0 or self.snake.location[0][1] >= self.GRID_X_Y
            or self.snake.location[0][1] < 0):
            return True
        return False


if __name__ == "__main__":
    core = Game_core()
    print("press enter to start: ")
    input()
    while core.game_state:
        core.print()
    print(f"\u001b[{core.GRID_X_Y//2}D", end="")
    print(f"\u001b[{core.GRID_X_Y//2}A", end="")
    sys.stdout.flush()
    print("YOU DIED")