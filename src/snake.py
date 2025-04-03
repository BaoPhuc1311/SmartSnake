class Snake:
    def __init__(self, start_pos, cell_size=30, width=600, height=400):
        self.body = [start_pos]
        self.direction = (cell_size, 0)
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.grow_next_move = False  

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if self.is_out_of_bounds(new_head) or new_head in self.body:  # Thêm kiểm tra tự cắn vào thân
            return False  

        self.body.insert(0, new_head)
        
        if not self.grow_next_move:
            self.body.pop()  
        else:
            self.grow_next_move = False  

        return True  

    def is_out_of_bounds(self, position):
        x, y = position
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def set_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def grow(self):
        self.grow_next_move = True  

    def get_body(self):
        return self.body

    def get_head(self):
        return self.body[0]
