import random

class Food:
    def __init__(self, width, height, block):
        self.width = width
        self.height = height
        self.block = block
        # Первая позиция
        self.position = self.spawn()

    # Создание случайной позиции
    def spawn(self):
        return (
            random.randrange(0, self.width, self.block),
            random.randrange(0, self.height, self.block)
        )
    
    # Перемещение еды на новую позицию
    def respawn(self, snake_body):
        while True:
            position = self.spawn()

            # Еда не должна появляться внутри змейки
            if position not in snake_body:
                self.position = position
                return
