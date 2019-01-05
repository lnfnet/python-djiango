#!/usr/bin/python3
#-*-coding:utf-8 -*-
import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Settings():
    """存储所有配置信息Settings.py"""
    def __init__(self):
        self.screen_width=600
        self.screen_height=800
        self.bg_color=(230,230,230)
        #飞船配置
        self.ship_speed_factor=1.5
        #子弹设置
        self.bullet_speed_factor=0.5
        self.bullet_width=10
        self.bullet_height=15
        self.bullet_color=(60,66,255)
        self.bullets_allowed=2
        
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings #实例化传入的 ai_settings
        #加载飞船并获取其外形矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #移动标志        
        self.moving_right = False
        self.moving_left =False
        self.moving_up =False
        self.moving_down =False
        #将每艘新飞船放在屏幕的底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #在centerx及centery中存储小数rect.centerx centery
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)
        
    def blitme(self):
        """在指定的位置重绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """移动飞船同时限定在屏幕内"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx-=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery+=self.ai_settings.ship_speed_factor
            #self.rect.centery+=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.centerx
        self.rect.centery=self.centery
        
class Bullet(Sprite):
    def __init__ (self,ai_settings,screen,ship):
        """飞船发射子弹的类"""
        super(Bullet,self).__init__()
        self.screen=screen
        #在（0，0）处创建一个子弹矩形，再设置正确的位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                  ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top     
        #存储小数表示子弹y 的位置
        self.y=float(self.rect.y)
        #设置子弹的着色和速度因子
        self.color = ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        
    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y = self.y
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #加载图片
        self.image = pygame.image.load(r'images\a.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
	
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
    if event.key==pygame.K_UP:
        ship.moving_up=True
    if event.key==pygame.K_DOWN:
        ship.moving_down=True
    if event.key==pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key==pygame.K_q:
        sys.exit()      
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
    if event.key==pygame.K_UP:
        ship.moving_up=False
    if event.key==pygame.K_DOWN:
        ship.moving_down=False
                
def update_screen(ai_settings,screen,ship,bullets,alien):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    pygame.display.flip()
    
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
#from ship import Ship
#from settings import Settings 导入配置类并实例化类

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #实例化类
    ship=Ship(ai_settings,screen)
    bullets=Group()
    alien=Alien(ai_settings,screen)
    # 开始游戏的主循环
    while True:
        check_events(ai_settings,screen,ship,bullets)# 监视键盘和鼠标事件
        update_screen(ai_settings,screen,ship,bullets,alien)
        update_bullets(bullets)
        ship.update() 
        #每次循环时重绘屏幕
        # 让最近绘制的屏幕可见        
run_game()
