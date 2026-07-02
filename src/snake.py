class Snake:
    def __init__(self, width, height, block):
        self.block = block

        # Начальное положение змейки (3 сегмента)
        self.body = [
            (width // 2, height // 2),
            (width // 2 - block, height // 2),
            (width // 2 - 2 * block, height // 2),
        ]

        self.dx = block
        self.dy = 0

    # Смена направления движения
    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx = dx
            self.dy = dy

    def step(self, grow=False):
        head_x, head_y = self.body[0]

        # Новая голова
        new_head = (head_x + self.dx, head_y + self.dy)
        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()
        return new_head

    def check_self_collision(self):
        return self.body[0] in self.body[1:]
    