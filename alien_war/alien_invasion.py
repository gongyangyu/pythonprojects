import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button


def run_game():
    # 初始化并创建屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_setting, screen,ship, aliens)
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_setting)
    # 创建Play按钮
    play_button = Button(ai_setting, screen, "Play")
    # 开始主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting,stats, play_button, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_setting, screen,stats, ship,aliens, bullets,play_button)


run_game()
