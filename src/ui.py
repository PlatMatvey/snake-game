import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_TEXT

class UI:
    def __init__(self):
        self.score_font = pygame.font.SysFont("Arial", 35)
        self.game_over_font = pygame.font.SysFont("Arial", 65, bold=True)

    # Отображение счёта
    def draw_score(self, screen, score):
        text = self.score_font.render(f"Счет: {score}", True, COLOR_TEXT)
        screen.blit(text, (20, 20))

    # Отображение надписи GAME OVER
    def draw_game_over(self, screen):
        text = self.game_over_font.render("Игра Окончена", True, COLOR_TEXT)
        rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        screen.blit(text, rect)
