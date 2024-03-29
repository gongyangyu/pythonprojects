import pygame


class Ship():
    def __init__(self, ai_setting, screen):
        """初始化"""
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/starfighter_64px.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx