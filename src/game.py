import pygame
from settings import *
from snake import Snake
from food import Food
from ui import UI

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Змейка")
        self.clock = pygame.time.Clock()

        self.snake = Snake(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK)
        self.food = Food(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK)
        self.ui = UI()

        self.score = 0
        self.running = True
        self.game_over = False

    # Обработка событий
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snake.set_direction(0, -BLOCK)

                elif event.key == pygame.K_s:
                    self.snake.set_direction(0, BLOCK)

                elif event.key == pygame.K_a:
                    self.snake.set_direction(-BLOCK, 0)

                elif event.key == pygame.K_d:
                    self.snake.set_direction(BLOCK, 0)

    # Обновление игры
    def update(self):
        grow = self.snake.body[0] == self.food.position
        self.snake.step(grow)

        if grow:
            self.score += 1
            self.food.respawn(self.snake.body)
        head_x, head_y = self.snake.body[0]

        if (
            head_x < 0 or
            head_x >= WINDOW_WIDTH or
            head_y < 0 or
            head_y >= WINDOW_HEIGHT or
            self.snake.check_self_collision()
        ):
            self.game_over = True

    # Отрисовка
    def draw(self):
        self.screen.fill(COLOR_BG)

        # Еда
        pygame.draw.rect(
            self.screen,
            COLOR_FOOD,
            (*self.food.position, BLOCK, BLOCK)
        )

        # Змейка
        for part in self.snake.body:
            pygame.draw.rect(
                self.screen,
                COLOR_SNAKE,
                (*part, BLOCK, BLOCK)
            )
        self.ui.draw_score(self.screen, self.score)

        if self.game_over:
            self.ui.draw_game_over(self.screen)
        pygame.display.flip()

    # Запуск игры
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()
        pygame.quit()
