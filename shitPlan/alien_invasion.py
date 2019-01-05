#!/usr/bin/python3
#-*-coding:utf-8 -*-
import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from time import sleep
import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color)
                
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True,
                self.text_color, self.ai_settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)


class Button():
    def __init__(self, ai_settings, screen, msg):
	"""初始化按钮的属性"""
	self.screen = screen
	self.screen_rect = screen.get_rect()
	# 设置按钮的尺寸和其他属性
	self.width, self.height = 200, 50
	self.button_color = (0, 255, 0)
	self.text_color = (255, 255, 255)
	self.font = pygame.font.SysFont(None, 48)
	# 创建按钮的rect对象，并使其居中
	self.rect = pygame.Rect(0, 0, self.width, self.height)
	self.rect.center = self.screen_rect.center
	# 按钮的标签只需创建一次
	self.prep_msg(msg)
    def prep_msg(self, msg):
	"""将msg渲染为图像，并使其在按钮上居中"""
	self.msg_image = self.font.render(msg, True, self.text_color,
					    self.button_color)
	self.msg_image_rect = self.msg_image.get_rect()
	self.msg_image_rect.center = self.rect.center
	
    def draw_button(self):
	# 绘制一个用颜色填充的按钮，再绘制文本
	self.screen.fill(self.button_color, self.rect)
	self.screen.blit(self.msg_image, self.msg_image_rect)
	
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
	"""初如化统计信息"""
	self.ai_settings=ai_settings
	self.reset_stats()
	self.game_active=False
	self.score = 0
	self.high_score = 0
    def reset_stats(self):
	self.score = 0
	self.level = 1
	self.ships_left=self.ai_settings.ship_limit
    
class Settings():
    """存储所有配置信息Settings.py"""
    def __init__(self):
        self.screen_width=600
        self.screen_height=800
        self.bg_color=(230,230,230)
        #飞船配置
	self.ship_limit=3
        #子弹设置

        self.bullet_width=600
        self.bullet_height=1200
        self.bullet_color=(60,66,255)
        self.bullets_allowed=2	

	self.speedup_scale = 1.1 #游戏速度增量
	self.fleet_drop_speed=10
	self.initialize_dynamic_settings()
	
	self.score_scale = 1.5
	
    def initialize_dynamic_settings(self):
	self.ship_speed_factor=1.5
	self.alien_speed_factor=0.1
	self.bullet_speed_factor=0.5
	#fleet_direction 1向右 -1为向左移	
	self.fleet_direction=1
	# 记分
	self.alien_points = 50
    def increase_speed(self):
	self.ship_speed_factor*=self.speedup_scale
	self.alien_speed_factor*=self.speedup_scale
	self.bullet_speed_factor*=self.speedup_scale
	
	self.alien_points = int(self.alien_points * self.score_scale)

	
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
	super(Ship,self).__init__()
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

    def center_ship(self):
	##不起作用
	self.rect.centerx=float(self.screen_rect.centerx)
        self.rect.bottom=float(self.screen_rect.bottom)
	

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
    def update(self):
	self.x+=(self.ai_settings.alien_speed_factor*
				self.ai_settings.fleet_direction)
	self.rect.x=self.x
	
    def check_edges(self):
	screen_rect=self.screen.get_rect()
	if self.rect.right>=screen_rect.right:
	    return True
	elif self.rect.left <=0 :
	    return True
            
def check_events(ai_settings,screen,stats,play_button,
				    ship,bullets,aliens,sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
	elif event.type==pygame.MOUSEBUTTONDOWN:
	    mouse_x,mouse_y=pygame.mouse.get_pos()
	    check_play_button(stats,play_button,mouse_x,mouse_y,aliens,
				    ai_settings,bullets,screen,ship,sb)
def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,ai_settings,
					    bullets,screen,ship,sb):
    """在玩家单击开始时运行游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
	ai_settings.initialize_dynamic_settings()
	#隐藏光标
	pygame.mouse.set_visible(False)	
	stats.reset_stats()
	stats.game_active=True
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	aliens.empty()
	bullets.empty()
	ship.center_ship()
	create_fleet(ai_settings, screen,ship, aliens)
	
	
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
                
def update_screen(ai_settings,stats,screen,ship,bullets,aliens,play_button,sb):
    sb.show_score()
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #如果游戏处于非活动状态。就绘制play按键
    if not stats.game_active:
	play_button.draw_button()
    aliens.draw(screen)
    #让最近的屏幕可见
    pygame.display.flip()
    
def update_bullets(aliens,bullets,ai_settings,screen,ship,sb,stats):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets,sb,stats)
   
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,sb,stats):
    """ 如果是碰撞，就删除相应的子弹和外星人&如果是敌人全部消灭重新生成"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    #如果敌人被清除重新生成
    if collisions:
	for aliens in collisions.values():
	    stats.score += ai_settings.alien_points * len(aliens)
	    sb.prep_score()
	check_high_score(stats,sb)
    if len(aliens)==0:
	# 提高等级
	stats.level += 1
	sb.prep_level()
	bullets.empty()
	ai_settings.increase_speed()
	create_fleet(ai_settings,screen,ship,aliens)
	
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen,ship, aliens):
    """建一个外星人然后根据1个在一行可以放入多少个"""
    """alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    
    for alien_number in range(number_aliens_x):
	alien=Alien(ai_settings,screen)
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	aliens.add(alien)"""
    alien = Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,
				ship.rect.height,alien.rect.height)
    
    for row_number in range(number_rows):
	for alien_number in range(number_aliens_x):
	    create_alien(ai_settings,screen,aliens,
			    alien_number,row_number)
	
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    avaliable_space_y = (ai_settings.screen_height-(3*alien_height)
			    -ship_height)
    number_rows=int(avaliable_space_y/(2*alien_height))
    return number_rows

def update_aliens(ai_settings,stats,screen,aliens,ship,bullets,sb):
    """更新敌机群"""
    #检查是否有外星人位于屏幕边界
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
	ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
	if alien.rect.bottom >= screen_rect.bottom:
	    ship_hit(ai_settings,stats,screen,ship,aliens.bullets)
	    break
	    
    
def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
	if alien.check_edges():
	    change_fleet_direction(ai_settings,aliens)
	    break
def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
	alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """飞船撞击后的处理"""
    if stats.ships_left >0:
	stats.ships_left -= 1 #生命减1
	sb.prep_ships()
	ship.center_ship() 	
	aliens.empty()#清空子弹及敌人
	bullets.empty()
	create_fleet(ai_settings,screen,ship,aliens)#重建游戏
	   
	#sleep(5)
    else:
	stats.game_active = False
	pygame.mouse.set_visible(True)#重设光标为可见
def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
	stats.high_score = stats.score
	sb.prep_high_score()
	
############################################################   
#from ship import Ship
#from settings import Settings 导入配置类并实例化类

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    #实例状态类
    stats=GameStats(ai_settings)
    #实例化类
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    # 创建外星人群
    create_fleet(ai_settings, screen, ship, aliens)
    #alien=Alien(ai_settings,screen)
    # 开始游戏的主循环
    sb = Scoreboard(ai_settings, screen, stats)
    while True:
	check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens,sb)# 监视键盘和鼠标事件
	if stats.game_active:
	    ship.update()
	    update_bullets(aliens,bullets,ai_settings,screen,ship,sb,stats)
	    update_aliens(ai_settings,stats,screen,aliens,ship,bullets)
	update_screen(ai_settings,stats,screen,ship,bullets,aliens,play_button,sb)
        #每次循环时重绘屏幕
        # 让最近绘制的屏幕可见        
run_game()
