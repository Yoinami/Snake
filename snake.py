class Snake:
    """Snake for the game"""
    def __init__(self) -> None:
        """"Yo"""
        self.location = []
        self.pointing = "d"
        self.last_added = False

    def move_snake(self):
        """move snake with keypressed direction"""
        if self.pointing == "w":
            x_add = 0
            y_add = -1
        elif self.pointing == "a":
            x_add = -1
            y_add = 0
        elif self.pointing == "s":
            x_add = 0
            y_add = 1
        else:
            x_add = 1
            y_add = 0
        self.location.insert(1, self.location[0].copy())
        self.location[0][0] += x_add
        self.location[0][1] += y_add
        self.location.pop()

    def add_snake(self):
        """add one segment of snake"""
        self.last_added = True
        self.location.append(self.location[-1].copy())

    def check_location(self, position: list):
        """check_location function take the argumanet x, y in a list and return 
        True if the snake exists in the given argument, return False if it doesn't
        for the print function"""
        if position in self.location:
            return True
        return False
    
    def dies_from_self(self):
        tem = []
        j = 1
        if self.last_added:
            self.last_added = False
            j = 2
        for i in self.location[:-j]:
            if i not in tem:
                tem.append(i)
            else:
                return True
        return False
    
    def _check_collision_with_apple(self, apple_x, apple_y):
        """check for the coolisoin apple with the head"""
        if self.location[0][0] == apple_x and self.location[0][1] == apple_y:
            self.add_snake()
            return True
        return False