#!/usr/bin/env python3

import pygame
import random
import sys

window = pygame.display.set_mode((830, 620))
pygame.display.set_caption('Dungeon Of the Skeleton GOD')

bg = pygame.Surface((600, 400))
bg3 = pygame.Surface ((180, 380))
bg4_text = pygame.Surface ((810, 170))
life = pygame.Surface ((15, 200))
mana = pygame.Surface ((15, 200))
life_black = pygame.Surface ((20, 130))
mana_black = pygame.Surface ((15, 130))
bg5 = pygame.Surface ((180, 150))
start_screen = pygame.Surface ((810, 600))
start_screen_text_surface = pygame.Surface ((200, 100))	

bg2 = pygame.image.load ('images/frame.png')
sprite_forward = pygame.image.load ('images/sprite2.png')
sprite_back = pygame.image.load ('images/sprite_back.png')





collide_skelet = 0
collide_zombi = 0
battle_mode = False
monster_info = False

green = (17, 220, 17)
cool_orange = (213,111,23)
white = (225, 225, 225)
sea_color = (20,100,100) 
black = (0,0,0)
red = (208,17,17)
swamp = ((113,111,23))
blue = ((30, 30, 180))



x = 45
y = 45
move_right = True
move_left = True
PLATFORM_WIDTH = 45
PLATFORM_HEIGHT = 45
minus = False
makepause = 0
key_q = 0
hppotionnum = 1
WIDTH = 45
HEIGHT = 45
up = False
down = False
right = False
left = False
STEP = 45
xlocal = 45
ylocal = 45
go_left = True
go_right = True
time_m = 0
stroke_monster = ''

key_ent = False 
key1 = False
key2 = False
key3 = False
act = False
move = True
special = False
turn = True
monster_turn = False
next_turn = 0
start_battle = True
monster_live = 1
pause = 0
stroke12_red = ''
info_hp = ''
stopshow_m = True
stopshow = True
time = 0
chek_monster_hp = 0



# 13 max 
stroke1 = 'Гидеон Рихтер'
stroke2 = '     паладин'
stroke3 = ' '
stroke4 = 'Атака: 6'
stroke5 = 'Защита: 4'
stroke6 = ""
stroke7 = 'Броня: 3'
stroke8 = 'Мана: 1'
stroke9 = 'Опыт:'
stroke10 = ''
stroke11 = ''
stroke12 = ''
stroke13 = ''
tst1 = 'Вы очнулись в одинокой камере в холодном и мрачном подземелье.'
tst2 = 'Вы чувствуете себя подавленным, кажется никто уже не придет к'
tst3 = 'вам на помощь. Все тело покрыто синяками и ссадинами, голова'
tst4 = 'раскалывается и страшно хочется пить. Вы совершенно не помните'
tst5 = 'как сюда попали...'
tst6 = ''
tst7 = ''
tst6_red = ''
tst7_back = ''

#sys

timer = pygame.time.Clock ()
pygame.key.set_repeat (100,100)


#Font
pygame.font.init ()
inf_font = pygame.font.Font ("fonts/fonta.ttf", 24)
inf_font2 = pygame.font.Font ("fonts/fonta.ttf", 20)
inf_font3 = pygame.font.Font ("fonts/fonta.ttf", 15)
inf_font_hp = pygame.font.Font ("fonts/fonta.ttf", 30)



level = [
       "-------------",
       "-    -  -   -",
       "-    -  -   -",
       "--- --- -- --",
       "-           ----    ",
       "-             -  ",
       "-- ----- -------",
       "-   -       -",
       "-------------"]




# Class








class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load ('images/wall.png')
		self.x = x
		self.y = y
		self.rect = self.image.get_rect ()
		self.rect.x = x
		self.rect.y = y
	
class Monster(pygame.sprite.Sprite):
	"""docstring for Sprite"""
	def __init__(self, x, y, filename, at, ac, hp, xp,name,dam):
		pygame.sprite.Sprite.__init__(self)
		self.att = at
		self.hp = hp
		self.ac = ac
		self.damage = dam

		self.image=pygame.image.load(filename)
		self.image.set_colorkey ((255,255,255))
		self.rect = pygame.Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.dasein = 1
		self.xp = xp
		self.name = name
		self.hp_old = hp

	def update(self):
		global minus, stopshow_m, stroke_monster, time_m, time_sec_m
		if self.hp_old >  self.hp:
			time_sec_m = 0
			time_m = 0
			stopshow_m = False
			#minus = True
			stroke_monster = str(-(self.hp - self.hp_old)) + "dem "
			
			self.hp_old = self.hp			
		if self.hp_old <  self.hp:
			time_sec_m = 0
			time_m = 0
			stopshow_m = False
			#minus = False
			stroke_monster = "+ " + str(self.hp - self.hp_old) + ""
			
			self.hp_old = self.hp

class potion(pygame.sprite.Sprite):
	"""docstring for Sprite"""
	def __init__(self, x, y, filename, potion_type, power):
		pygame.sprite.Sprite.__init__(self)
		self.name = potion_type
		self.power = power
		self.image=pygame.image.load(filename)
		self.image.set_colorkey ((255,255,255))
		self.rect = pygame.Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.dasein = 1

class Item(pygame.sprite.Sprite):
	"""docstring for Sprite"""
	def __init__(self, x, y, filename, name):
		self.name = name
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(filename)
		self.image.set_colorkey ((255,255,255))
		self.rect = pygame.Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.dasein = 1
		#self.weapon = weapon
		#self.damage = damage
	
class Sprite(pygame.sprite.Sprite):
	"""docstring for Sprite"""
	def __init__(self, x, y, filename, att, ac, hp, mp):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load(filename)
		self.image.set_colorkey ((255,255,255))
		self.rect = pygame.Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.word = 'dwede'
		self.go_left = True
		self.xlocal = x
		self.ylocal = y
		self.xlocal_old = x
		self.ylocal_old = y
		self.att = att
		self.ac = ac
		self.hp = hp
		self.mp = mp
		self.xp = 0
		self.collide_monster = 0
		self.weapon = "Кор.меч"
		self.damage = 1
		self.hp_old = hp
		self.max_hp = hp


	def update (self, left, right, blocks, monsters):
		global minus, time_sec, time, stroke6, stopshow, stroke1,stroke2,stroke3,stroke4,stroke5,stroke7,stroke8,stroke9,stroke10,stroke13, stroke12, stroke12_red
		
		self.rect.x = self.xlocal
		self.rect.y = self.ylocal
		self.collide (blocks, monsters)
		stroke6 = 'Жизни: ' + str(hero.hp)

		
		self.xlocal_old = self.xlocal
		self.ylocal_old = self.ylocal

		stroke1 = 'Гидеон Рихтер'
		stroke2 = '     паладин'
		stroke3 = ' '
		stroke4 = 'Атака: '+ str(self.att)
		stroke5 = 'Защита: '+ str (self.ac)
		stroke6 = 'Жизни: ' + str(self.hp)
		stroke7 = ''
		stroke8 = 'Мана: ' + str (self.mp)
		stroke9 = 'Опыт: ' + str (self.xp)
		stroke10 = 'Зелья: ' + str(hppotionnum)
		stroke13 = str(self.weapon)+ ' урон: '+ str (self.damage)

		if self.hp > self.max_hp:
			self.hp = self.max_hp

		if self.hp_old >  self.hp:
			time_sec = 0
			time = 0
			stopshow = False
			minus = True
			stroke12_red = str(self.hp - self.hp_old) + " hp"
			
			self.hp_old = self.hp			
		if self.hp_old <  self.hp:
			time_sec = 0
			time = 0
			stopshow = False
			minus = False
			stroke12_red = "+ " + str(self.hp - self.hp_old) + " hp"
			
			self.hp_old = self.hp


	def collide (self, blocks, monsters):
		global collide_skelet, collide_zombi
		for pl in blocks:
			if pygame.sprite.collide_rect (self, pl):
				if self.xlocal < self.xlocal_old:
					
					
					self.xlocal = self.xlocal +45
				if self.xlocal > self.xlocal_old:
					
					
					self.xlocal = self.xlocal - 45
				if self.ylocal < self.ylocal_old:
					
					
					self.ylocal = self.ylocal +45
				if self.ylocal > self.ylocal_old:
					
					
					self.ylocal = self.ylocal - 45

		for element in monsters:
			if pygame.sprite.collide_rect (self, element) and element.dasein == 1:
				if self.xlocal < self.xlocal_old:
				
					self.xlocal = self.xlocal +45
					interaction_monster (element.name, element)
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1

				if self.xlocal > self.xlocal_old:
									
					self.xlocal = self.xlocal - 45
					interaction_monster (element.name, element)
					collide_monster = 1
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1
				if self.ylocal < self.ylocal_old:
							
					self.ylocal = self.ylocal +45
					interaction_monster (element.name, element)
					collide_monster = 1
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1

				if self.ylocal > self.ylocal_old:
					self.ylocal = self.ylocal - 45
					interaction_monster (element.name, element)
					collide_monster = 1
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1

		for element in items:
			if pygame.sprite.collide_rect (self, element):
				
				
					
					interaction_item (element)
					items.remove (element)
					a_group.remove (element)
	




# item

hppotion = potion (270, 45, 'images/hppotion.png', 'hp', '1К6')
hppotion2 = potion (270, 90, 'images/hppotion.png', 'hp', '1К6')
hppotion3 = potion (315, 45, 'images/hppotion.png', 'hp', '1К6')
sword = Item (225, 315, 'images/sword.png', 'weapon')

sword.weapon = 'Дл.меч'
sword.damage = 2


#monsters
skelet1 = Monster (540,225, 'images/skeleton.png', 5, 4, 4, 10, 'СКЕЛЕТ', 2)
skelet2 = Monster (315,135, 'images/skeleton.png', 5, 4, 4, 10, 'СКЕЛЕТ', 2)

zombi1 = Monster (45, 315, 'images/zombi.png', 10, 0, 10, 25, "ЗОМБИ" , 1)
wizard = Monster (450, 45, 'images/wiz.png', 10,10,5,250, "ВОЛШЕБНИК", 3)
zombi2 = Monster (270, 315, 'images/zombi.png', 10, 0, 10, 25, "ЗОМБИ", 1)
current_monster = skelet1

#Hero
hero = Sprite (x, y, 'images/sprite2.png', 6,5,7,2)	
hero.move_right = True



#compeal of lists

a_group = pygame.sprite.Group ()
b = pygame.sprite.Group ()
b.add (hero)
a_group.add (skelet1, skelet2)
a_group.add (zombi1)
a_group.add (wizard)
a_group.add (hppotion)
a_group.add (hppotion2, hppotion3,sword)
a_group.add (zombi2)

blocks = []
monsters = []
items = []
monsters.append (wizard)
items.append (hppotion)
items.append (hppotion2)
items.append (hppotion3)
items.append (sword)
monsters.append (skelet1)
monsters.append (zombi1)

monsters.append (zombi2)
monsters.append (skelet2)

x=y=0
for row in level:
	for col in row:
		if col == "-":
			pf = Platform (x, y)
			a_group.add (pf)
			blocks.append (pf)
		x += PLATFORM_WIDTH
	y += PLATFORM_HEIGHT
	x=0

zombi_talk = 0 

def quest ():
	global act, key3, move,  key1, key2, battle_mode, pause, key_ent, collide_skelet, collide_zombi, zombi_talk, current_monster
	a = random.randint (1,6)
	if act == True and collide_skelet:
		if key3 == True:
			move = True
			key3 = False
			key1 = False
			key2 = False
			act = False
			collide_skelet = 0
			talk ()
		if key1 == True:
			key3 = False
			key1 = False
			key2 = False
			act = False
			battle_mode = True
		if key2:
			act = 0
			key2 = 0
			pause = 1
			clear_talk ()
			talks (1, 'Скелет не реагирует на ваши слова. Пустые глазницы')
			talks (2, 'безмолвно обращены на вас, в их глубине полыхают огоньки')
			talks (3, 'мертвого пламени. Рука скелета недвижимо лежит на рукоятке')
			talks (4, 'меча, притороченного к его поясу.')
			talks (8, 'Нажмите E.')

	if key_ent and pause and collide_skelet:
		interaction_monster ('СКЕЛЕТ', current_monster)
		pause = 0

	if act == True and collide_zombi and zombi_talk == 0:
		if key3 == True:
			move = True
			key3 = False
			key1 = False
			key2 = False
			act = False
			collide_zombi = 0
			talk ()
		if key1 == True:
			key3 = False
			key1 = False
			key2 = False
			act = False
			battle_mode = True
		if key2:

			act = True
			key2 = 0
			
			clear_talk ()
			talks (1, 'Зомби что-то вяло и нечленораздельно булькает.')
			talks (2, 'Вы можете разобрать слова злого духа, который управляет')
			talks (3, 'бренной плотью: "Кр... ооо.. в.. ии!')
			talks (5, '1 - дать ему своей крови; 2 - прочитать заупокойную.')
			zombi_talk = 1
			


	if act == True and collide_zombi and zombi_talk == 1 and key1 and (a == 1 or a == 2 or a == 3):
			clear_talk ()
			talks (1, 'Вы полоснули ножом по своей руке, набрали в рукавицу крови')
			talks (2, 'и поднесли источающему зловоние трупу. Он жадно припал к ней')
			talks (3, 'и начал пить. Затем резко отпрянул, его тело задергалось и')
			talks (4, 'упало, словно темный дух его отпустил.')
			zombi_talk = 0
			pygame.sprite.Sprite.kill (current_monster)
			hero.xp = hero.xp + current_monster.xp
			hero.hp = hero.hp - 1
			move = True
			key3 = False
			key1 = False
			key2 = False
			act = False
			collide_zombi= 0
			monsters.remove (current_monster)

	if act == True and collide_zombi and zombi_talk == 1 and key2 and (a == 4 or a == 5 or a == 6) and hero.mp > 0:
			clear_talk ()
			talks (1, 'Вы читаете слова молитвы. Труп дергается и оседает на пол.')
			talks (2, 'Кажется, злой дух его оставил.')

			zombi_talk = 0
			pygame.sprite.Sprite.kill (current_monster)
			hero.xp = hero.xp + current_monster.xp
			hero.mp = hero.mp - 1
			move = True
			key3 = False
			key1 = False
			key2 = False
			act = False
			collide_zombi= 0
			monsters.remove (current_monster)

	if act == True and collide_zombi and zombi_talk == 1 and key2 and ((a == 1 or a == 2 or a == 3) or hero.mp <= 0):
			clear_talk ()
			talks (1, 'Вы читаете слова молитвы. Но ничего не происходит.')
			talks (2, 'Вам кажется, что злой дух смеётся над вашей верой.')
			if hero.mp > 0:
				hero.mp = hero.mp - 1

			zombi_talk = 0
			move = True
			key3 = False
			key1 = False
			key2 = False
			act = False
			collide_zombi= 0


	if act == True and collide_zombi and zombi_talk == 1 and key1 and (a == 4 or a == 5 or a == 6):
			clear_talk ()
			talks (1, 'Вы полоснули ножом по своей руке, набрали в рукавицу крови')
			talks (2, 'и поднесли источающему зловоние трупу. Он жадно припал к ней')
			talks (3, 'и начал пить. Затем глаза его загорелись и он с удвоенной силой')
			talks (4, 'бросился на вас, желая сожрать вас целиком.')
			talks (8, "Нажмите Е")
			zombi_talk = 3
			current_monster.att = current_monster.att + 3
			hero.hp = hero.hp - 1
			

			

	if act == True and collide_zombi and zombi_talk == 3 and key_ent:
			key_ent = False
			key1 = False
			key2 = False
			act = False
			battle_mode = True
			zombi_talk = 0




	if key_ent and pause and collide_zombi:
		interaction_monster ('ЗОМБИ', current_monster)
		pause = 0

def big_talks (a):
	global tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst7_back

	tst1 = a[0:63]
	tst2 = a[63:126]	



def clear_talk ():
	global tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst6_red, tst7_back
	tst6_red = ''
	tst7_back = ''
	tst1 = ''
	tst2 = ''
	tst3 = ''
	tst4 = ''
	tst5 = ''
	tst6 = ''
	tst7 = ''

def talks (a,b):
	global tst1, tst2, tst3, tst4, tst5, tst6, tst7, tst7_back
	if a ==1:	
		tst1 = b
	elif a ==2:	
		tst2 = b
	elif a ==3:	
		tst3 = b
	elif a ==4:	
		tst4 = b
	elif a ==5:	
		tst5 = b
	elif a ==6:	
		tst6 = b
	elif a ==7:	
		tst7 = b
	elif a ==8:	
		tst7_back = b

def interaction_item (item):
	global hppotionnum
	
	clear_talk ()
	if item.name == 'hp':
		talks (1, 'Вы видите целебное зелье,')
		talks (2, 'которое восстанавливает ' + str(item.power)+' жизней')
		talks (3, 'Вы подбираете его.')
		hppotionnum = hppotionnum + 1
	if item.name == 'weapon':
		hero.weapon = item.weapon
		hero.damage = item.damage

		talks (1, 'Вы видите ' +item.weapon+' его урон: ' + str(item.damage))
		talks (2, "Хорошая вещица!")
		talks (3, 'Вы подбираете этот беcхозный предмет,')
		talks (4, 'чтобы он послужил благой цели.')

words_chek = True
num_for_word = 1
key_space = False


def battle (hero, monster):
	global special_wiz, battle_wiz_start, num_for_word, words_chek, tst6_red, chek_monster_hp, a_group, monsters, collide_skelet, collide_zombi, next_turn, monster_live, monster_info, minfo1, minfo2, minfo3, minfo4, minfo5, move, done, key_ent, key1, key2, key3, battle_mode, start_battle, special, turn, monster_turn, key_space
	monster_info = True
	minfo1 = str(monster.name)
	minfo2 = 'Жизни: '
	minfo5 = str(monster.hp)
	minfo3 = 'Атака: '+str(monster.att)
	minfo4 = 'Защита: '+str(monster.ac)


	if turn == True:
		clear_talk ()
		talks (1, 'Твой ход! Что ты будешь делать:')
		talks (3, '1 - атаковать, 2 - особая способность, 3 - убегать')

	if key1 == True and turn == True:
		turn = False

		clear_talk ()
		a = random.randint (1,6)
		b = random.randint (1,6)
		c = hero.att + a 
		d = monster.ac + b
	
		talks (1, "Ваша атака: "+str(c) + "  Защита монстра: "+ str(d))
		if c >= d:
			
			if int(c/d)>1:
				monster.hp = monster.hp - hero.damage*int(c/d)
				talks (4, 'Критический удар! Урон умножается на  '+str(int(c/d)))
				tst6_red = 'Критический урон: '+str(hero.damage*int(c/d))
				
			else:
				talks (4, "Вы попали и нанесли сокрушительный удар!")
				monster.hp = monster.hp - hero.damage
				tst6_red = 'Урон: '+str(hero.damage)
		elif c<d:
			talks (4, 'Вы промазали!')	
		key1 = False
		talks (8, 'Нажмите Е')

	if monster_turn == True and monster == wizard and words_chek == True:
		num_for_word = random.randint (1,3)
		words_chek = False

	if monster_turn == True and monster == wizard:
		clear_talk ()
		talks (1, 'Волшебник:')
		talks (2, 'Как бишь там это заклинание называется?')
		words = {1:'Огненный пар...?', 2: 'Пламенный жар...?', 3:'А... Огненный шар!'}
		talks (3, str(words[num_for_word]))
		end_talk ()
		if key_ent ==True:
			key_ent = False
			clear_talk ()
			talks (1, 'В вас ударяет сноп раскаленного пламени, который')
			talks (2, 'страшно обжигает вас. Ваша кожа обугливается.')
			a = random.randint (1,6)

			hero.hp = hero.hp - a
			tst6_red = 'Вы получили '+str(a) +' урона'


			talks (8, 'Нажмите Е')
			monster_turn = False
			next_turn = True
			words_chek = True

	if monster_turn == True and monster != wizard:
		clear_talk ()


	

		a = random.randint (1,6)
		b = random.randint (1,6)
		c = hero.ac + a 
		d = monster.att + b
		talks (1, "Атака монстра: "+str(d) + "  Ваша защита: "+ str(c))
		if c > d:
			talks (4, "Монстр не попал по вам.")		
		elif c<=d:
			
			if int(d/c)>1:
				hero.hp = hero.hp - (monster.damage*int(d/c))
				talks (4, 'Критический удар! Урон умножается на  '+str(int(d/c)))
				tst6_red = 'Критический урон: '+str(monster.damage*int(d/c))
			else:
				talks (4, 'По вам попали!')
				hero.hp = hero.hp - monster.damage
				tst6_red = 'Вы получили '+str(monster.damage)+ ' урона'

		talks (8, 'Нажмите Е')
		monster_turn = False
		next_turn = True

	if key3 and turn:
		turn = 0
		if hero.hp > 1:
			clear_talk ()
			talks (1, 'Вы ж паладин! Вы не можете убежать. Ведь ')
			talks (2, 'вы следуете велениям вашего сердца.')
			talks (3, 'А ваше сердце вам этого не подсказывает.')
			talks (8, 'Нажмите E')
			next_turn = 1
		if hero.hp == 1:
			clear_talk ()
			talks (1, 'Вы прислушались к вашему сердцу. Оно')
			talks (2, 'явно советует вам тактически отступить.')
			talks (3, 'Что ж, так тому и быть! Вы убежали.')

			move = True
			monster_info = 0
			turn = True
			collide_skelet = 0
			collide_zombi = 0
			battle_wiz_start = False
			special_wiz = False
			battle_mode = False
			return

	if monster.hp <= 0:
		pygame.sprite.Sprite.kill (monster)
	if key2 and turn:
		turn = False
		clear_talk ()
		talks (1, 'Какую спец. способность ты хочешь использовать:')
		talks (3, '1 - изгонение нежити, 2 - лечение, 3 - назад')
		special = 1
		key2 = False

	if key2 and special and hero.mp<=0:
		talks (5, 'Не хватает веры!')
		key2 = False

	if key2 and special and hero.mp>0:
		key2 = False
		clear_talk ()
		hero.mp = hero.mp -1
		talks (1, "Вы восстановили 4 жизни!")
		hero.hp = hero.hp +4
		next_turn = 1
		special = 0
		talks	(8, 'Нажмите E')

	if key3 and special:
		turn = 1
		key3 = 0
		special = 0

	if key1 and special and hero.mp <= 0:
		talks (5, 'Не хватает веры!')	
		key1 = 0

	if key1 and special and hero.mp > 0:
		key1= 0
		special = 0
		hero.mp = hero.mp - 1

		if monster.hp <= 3:
			monster.hp = 0

			talks (5, 'Монстр рассыпался в прах!')
			pygame.sprite.Sprite.kill (monster)

		else:
			
			next_turn = 1
			talks (5, 'К сожалению ничего не произошло.')
		talks	(8, 'Нажмите E')

	if key_ent == True and next_turn == 1:
		turn = True
		next_turn = 0
		key_ent = 0


	if key_ent == 1 and turn == 0 and monster.hp>0:
		monster_turn = True
		key_ent = 0

	if key_ent == 1 and turn == 0:
		chek_monster_hp = 1
		key_ent = 0

	if hero.hp <= 0:
		clear_talk ()
		talks (1, 'Вы умерли.')
		talks (2,'Никто не вспомнит о вас,')
		talks (3, 'погребенном в пучине забвения.')
		talks (5, 'GAME OVER')
		talks (8, 'SPACE')
		pygame.sprite.Sprite.kill (hero)
		battle_mode = False
		special_wiz = False
		wiz_conversation = False

	if hero.hp <= 0 and key_space == True:
		done = False

	if monster.hp <=0 and chek_monster_hp == 1:
		clear_talk ()
		chek_monster_hp = 0
		talks (1, 'Вы победили ужасного монстра!')
		talks (2, 'Вы получаете опыт: '+ str(monster.xp))
		hero.xp = hero.xp + monster.xp
		battle_mode = False
		move = True
		monster_info = 0
		monster.dasein = 0
		a_group.remove (monster)
		monsters.remove (monster)
		collide_skelet = 0
		collide_zombi = 0
		wiz_conversation = False
		special_wiz = False

		turn = True

	monster.update ()	
	monster_hp_modify (monster)

def talk ():
	global tst1, tst2, tst3, tst4, tst5
	tst1 = 'Страх охватил вас полностью...'
	tst2 = 'Вы, чувствуя как в животе возникла холодная пустота, начали'
	tst3 = 'медленно отсутупать, не отводя взгляда от гиипнотических'
	tst4 = 'огоньков в глазницах скелета. Молчаливый костяк не стал вас'
	tst5 = 'преследовать.'

wiz_level_conv = 123
special_wiz = False
current_npc = wizard
battle_wiz_start = False

def interaction_monster (name, monster):
	global monsters, monster_killed, wiz_level_conv, tst1, tst2, tst3, tst4, tst5, move, act, current_monster, special_wiz, current_npc, battle_wiz_start
	

	if name == 'ВОЛШЕБНИК':


		#for x in monsters:
			#if x.name != "ЗОМБИ" or x.name != "СКЕЛЕТ":
			#	monster_killed = False

		if wiz_level_conv == -1:
			battle_wiz_start = True
		
		special_wiz = True
		move = False

		#if hero.xp < 30:
			#talks (1, 'Приходи, когда будешь достоин.')
		#if hero.xp > 30:
			#talks (1, 'Что ж, ты достоин! Я телепортирую тебя отсюда.')
			#pygame.sprite.Sprite.kill (hero)

			#talks (3, 'Вы выбрались из подземелья!')
			#move = False
			#hero.xp = hero.xp + 100

	if name == 'СКЕЛЕТ':
		clear_talk ()
		tst1 = 'Вы видите злобного, источающего смрад скелета, чьи угольки'
		tst2 = 'красных глаз зловеще смотрят на вас, внушая ужас потусторонней'
		tst3 = 'жизни. Что вы сделаете?'
		tst4 = ''
		tst5 = '1 - вступить в бой! ; 2 - поговорить; 3 - уйти.'
		move = False
		act = True
		current_monster = monster
	if name == 'ЗОМБИ':
		clear_talk ()
		tst1 = 'Вы видите разлагающийся зловещий труп, источающий смрад.'
		tst2 = 'Куски его гнилого мяса патологически раздулись, в ранах'
		tst3 = 'копошатся черви. На руках огромные нечеловеческие когти.'
		tst4 = ''
		tst5 = '1 - вступить в бой! ; 2 - поговорить; 3 - уйти.'
		move = False
		act = True
		current_monster = monster



next_talk = False
wiz_level_conv = 123



a_book = 0
monster_num = 0

def wiz_conversation ():
	global a_book, key_ent, next_talk, wiz_level_conv, key1, key2, key3, battle_wiz_start, special_wiz, move
	global hppotionnum, monsters, monster_killed, done, monster_num

	for x in monsters:
		if x.name == "ЗОМБИ" or x.name == "СКЕЛЕТ":
			monster_num += 1
			
	if monster_num == 0:
		monster_killed = True
	else:
		monster_killed = False
		monster_num = 0






	if wiz_level_conv == 123 and monster_killed == False:
		clear_talk ()
		talks (1, 'Вы видите седого как лунь старика, сидяшего за письменным столом')
		talks (2, 'в комнате, оборудованной как лаборатория. На столе книги и крошки.')
		talks (3, 'Вы успеваете заметить, как он, при вашем появлении, что-то быстро')
		talks (4, 'спрятал под стол.')
		talks (8, 'Нажмите Е')
		wiz_level_conv = 1

	if monster_killed == True and (wiz_level_conv == 4 or wiz_level_conv == 222 or wiz_level_conv == 123):
		clear_talk ()
		talks (1, 'О! Молодой человек, я смотрю вы уничтожили всех монстров в этом')
		talks (2, 'досточнимом подземелье? Очень учтиво с вашей стороны.')
		talks (3, 'За это я вас облагодетельствую. И помогу вам в вашей беде.')
		talks (4, 'Вы ведь хотите выбраться отсюда?')
		talks (8, 'Нажмите Е')
		wiz_level_conv = 55

	if wiz_level_conv == 55 and key_ent == True:
		clear_talk ()
		key_ent = False
		move = True
		done = False


	if wiz_level_conv == 222:
		clear_talk()
		talks (1, 'Волшебник недовольно смотрит на вас и дает понять, что не хочет')
		talks (2, 'с вами разговаривать.')
		talks (5, '1 - уйти, 2 - напасть на волшебника!')


	if key_ent == 1 and wiz_level_conv == 1:
		clear_talk ()
	
		talks (1, 'Кто ты такой? И зачем ты осмелился потревожить меня, могучего')
		talks (2, 'мага, уединившегося в этом заброшенном подземелье. Хм... Видимо')
		talks (3, 'ты пришел, чтобы обрести мудрость. Что ж, спрашивай, но у тебя есть')
		talks (4, 'только один вопрос!')
		talks (7, "3 - напасть на богомерзкого колдуна!")
		talks (6, '1 - как мне выбраться из подземелья?; 2- а что это вы спрятали?;' )
		wiz_level_conv = 2

	if wiz_level_conv ==4:
		clear_talk ()
		talks (1, 'Седой загадочный волшебник выглядит расстроенно.')
		talks (2, '"Ну я же сказал, что нужно истребить всех монстров!')
		talks (3, 'Возвращайся как истребишь."')
		talks (5, '1 - уйти, 2 - напасть на волшебника!')
		wiz_level_conv = 5

	if key1 == True and wiz_level_conv ==2:
		clear_talk ()
		talks (1, 'Ну что ж, могу я помочь тебе в этом деле. Да вот только и ты мне,')
		talks (2, 'мил человек, услугу окажи. Слишком много у меня тут монстров')
		talks (3, 'развелось. Жития от них нет! Истреби ка их всех, а там поговорим.')
		special_wiz = False
		wiz_level_conv = 4
		move = True
		key1 = False
		talks (8, 'Конец разговора')
		




	if (wiz_level_conv == 5 or wiz_level_conv == 222) and key1==True:
		clear_talk ()
		talks (1, "Вы мироблюбиво попрощались с магом и ушли прочь.")
		special_wiz = False
		wiz_level_conv = 4
		move = True
		key1 = False

	if key2 == True and wiz_level_conv ==2:
		key2 = False		
		clear_talk ()
		talks (1, 'Э... Что-то ты не то спрашиваешь. Чтобы там ни было - это к делу не')
		talks (2, 'относится. Это сугубо мои личные волшебнические дела.')

		talks (4, "1 - попробуете угадать, что у мага под столом;")
		talks (5, "2 - извинитесь и перейдете к серьезным вопросам.")


	
		wiz_level_conv =22


	if key1 == True and wiz_level_conv == 22:
		key1 = False
		clear_talk ()
		talks (1, "Что спрятал волшебник?")
		talks (5, '1 - труп!; 2 - некрономикон!; 3 - жареную курицу!')

		wiz_level_conv = 221

	if key1 == True and wiz_level_conv == 221:
		key1 = False
		clear_talk ()
		talks (1, "Что? Труп? Да что ты себе позволяешь, нахаленок?")
		talks (2, 'Ты нанес мне смертельное оскорбление, обвинив')
		talks (3, 'меня в некромантии. Я с тобой больше не говорю.')

		talks (8, 'Конец разговора')
		special_wiz = False
		wiz_level_conv = 222
		move = True


	if key2 == True and wiz_level_conv == 221:
		key2 = False
		clear_talk ()
		talks (1, "'Да, всенепременно! Хочешь посмотреть?'")
		talks (2, 'Волшебник лукаво достает из под стола какую-то старую')
		talks (3, 'обшарпаную книгу в кожаном переплете.')

		talks (5, '1 - подойти посмотреть, 2 - ты меня обманываешь!')

		wiz_level_conv = 2212

	if key3 == True and wiz_level_conv == 221:
		key3 = False
		clear_talk ()
		talks (1, '"Э..." Волшебник выглядит смущённо. Вы замечаете, что')
		talks (2, 'в команте действительно стоит еле заметный запах жареной')
		talks (3, 'куры, натёртой чесноком. "Ладно, говоришь тебя надо куда-то')
		talks (4, 'отправить? Давай, сейчас устроим. Нечего тебе тут делать".')
		talks (5, 'Волшебник читает заклинание и открывает портал.')
		talks (7, '+ 100 опыта')
		talks (8, "Нажмите E")
		hero.xp = hero.xp+100
		wiz_level_conv = 2213

	if wiz_level_conv == 2213 and key_ent == True:
		clear_talk ()
		key_ent = False
		move = True
		done = False


	if key2 == True and wiz_level_conv == 2212:
		key2 = False
		clear_talk ()
		talks (1, 'Да, молодой человек, нахальное поведение с вашей стороны.')
		talks (2, 'А еще паладином называетесь. Все, я занят, у меня нет')
		talks (3, 'времени разговаривать с вами по пустякам. Делай что хочешь.')
		talks (8, "Конец разговора.")
		special_wiz = False
		move = True
		wiz_level_conv = 222

	if key1 == True and wiz_level_conv == 2212:
		key1 = False
		clear_talk ()
		talks (1, 'Вы подходите к столу, начинаете рассматривать старую книгу')
		talks (2, 'Открываете, склоняетесь над ней. Внезапно она оживает и кусает')
		talks (3, 'ваше лицо! А после этого улетает в неизвестном направлении.')
		talks (4, "Волшебник хохочет.")
		talks (8, "Конец разговора")
		a_book = random.randint(1,6)	
		if a_book == 6:
			hero.att = hero.att +2	
		hero.hp = hero.hp - 1
		wiz_level_conv = 22121		
		special_wiz = False
		move = True
		return


	if wiz_level_conv ==22121:
		clear_talk ()
		if a_book != 6:
			talks (1, 'Хе-хе! Посмеялся я от души. Ну извини, на, вот тебе зелье целебное,')
			talks (2, 'до свадьбы заживет. А к тебе у меня дело есть. Полно тут трупов ходит.')
			talks (3, 'Жития от них нет! Истреби ка их всех, а там я тебе и помогу')
			hppotionnum = hppotionnum + 1
		else:
			talks (1, 'Волшебник смотрит на вас озадаченно:')
			talks (2, '"Похоже укус книги вызвал у вас ряд положительных мутаций')
			talks (3, 'Что ж, скажите мне спасибо. Да, а теперь убейте всех монстров')
			talks (4, 'в округе - после этого поговорим."')
		special_wiz = False
		wiz_level_conv = 4
		move = True
		key1 = False
		talks (8, 'Конец разговора')




	if key2 == True and wiz_level_conv == 22:
		key2 = False
		clear_talk ()
		talks (1, 'Да, молодой человек, нахальное поведение с вашей стороны.')
		talks (2, 'А еще паладином называетесь. Все, я занят, у меня нет')
		talks (3, 'времени разговаривать с вами по пустякам. Делай что хочешь.')
		talks (8, "Конец разговора.")
		special_wiz = False
		move = True
		wiz_level_conv = 222




	if (key3 == True and wiz_level_conv ==2) or ((wiz_level_conv == 5 or wiz_level_conv ==222) and key2==True):
		battle_wiz_start = True
		wiz_level_conv = -1
		key3 = False
		key2 = False
	if battle_wiz_start == True:
		battle (hero, wizard)
	if wizard.dasein == False:
		battle_wiz_start = False





def monster_hp_modify (unit):
	global stroke_monster, stopshow_m, minus
	#if stopshow == False and minus == False:
		#bg.blit(inf_font.render (stroke_monster, True, (green)), (unit.rect.x,unit.rect.y-30-time_sec))
	if stopshow_m == False:
		bg.blit(inf_font_hp.render (stroke_monster, True, (white)), (unit.rect.x,unit.rect.y-10-time_sec_m))

def hp_modify ():
	global stroke12_red, stopshow, minus
	if stopshow == False and minus == False:
		bg.blit(inf_font_hp.render (stroke12_red, True, (green)), (hero.rect.x,hero.rect.y-10-time_sec))
	if stopshow == False and minus:
		bg.blit(inf_font_hp.render (stroke12_red, True, (red)), (hero.rect.x,hero.rect.y-10-time_sec))

def end_talk ():
	talks (8, "Нажмите E")


#start_screen_rect = start_screen_text_surface.get_rect ()

menu_text = "  Нажмите SPACE"

class Menu ():
	def __init__ (self):
		
		self.time = 0
		self.x = 225
		self.up = True
	def color_change (self):
		if self.up == True:
			self.x = self.x - 5
		if self.up == False:
			self.x = self.x + 5

		if self.x > 210:
			self.up = True
		if self.x < 10:
			self.up = False




	def render (self):
		main_image = pygame.image.load ('images/main_pic2.gif')
		start_screen.blit (main_image, (120, 100))

	def main (self):
		done1 = True

		while done1:

			for e in pygame.event.get ():
					if e.type == pygame.QUIT:
							sys.exit ()

					if e.type == pygame.KEYDOWN:
						if e.key == pygame.K_SPACE:

							done1 = False

			window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit(start_screen_text_surface, (300, 510))
			start_screen_text_surface.fill ((black))
			start_screen_text_surface.blit(inf_font.render (menu_text,True, (self.x,self.x,self.x)), (10,10))
			self.render ()
			self.color_change ()

			timer.tick (30)
			self.time = self.time + 1

			pygame.display.update() 

end_text = "Конец демо-версии"

class End ():
	def __init__ (self):
		
		self.time = 0
		self.x = 225
		self.up = True





	#def render (self):
		#main_image = pygame.image.load ('images/main_pic2.gif')
		#start_screen.blit (main_image, (120, 100))
	def main (self):
		done2 = True

		while done2:

			for e in pygame.event.get ():
					if e.type == pygame.QUIT:
							sys.exit ()

					if e.type == pygame.KEYDOWN:
						if e.key == pygame.K_SPACE:

							done2 = False

			window.blit(start_screen, (10, 10))
			start_screen.fill ((black))
			start_screen.blit(start_screen_text_surface, (300, 250))
			start_screen_text_surface.fill ((black))
			start_screen_text_surface.blit(inf_font.render (end_text,True, (self.x,self.x,self.x)), (10,10))
			


			timer.tick (30)


			pygame.display.update() 


end_title = End ()			
pygame.mixer.pre_init (44100, -16, 1, 2512)
pygame.mixer.init()
sound = pygame.mixer.Sound('sounds/intro.ogg')
sound.play(-1)
sound.set_volume(0.5)

start_menu = Menu ()
start_menu.main ()



done = True
while done:

	for e in pygame.event.get ():
			if e.type == pygame.QUIT:
					sys.exit ()

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_LEFT and move == True:
					hero.image= sprite_back
					hero.image.set_colorkey ((255,255,255))
					if hero.xlocal >0:
						hero.xlocal -= STEP


				if e.key == pygame.K_RIGHT and move == True:
					hero.image= sprite_forward
					hero.image.set_colorkey ((255,255,255))
					hero.xlocal += STEP

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP:
					if hero.ylocal >0 and move == True:
						hero.ylocal -= STEP
				if e.key == pygame.K_DOWN:
					if hero.ylocal <360 and move == True:
						hero.ylocal += STEP	

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_SPACE and hero.hp >0:
					start_menu.main ()
				if e.key == pygame.K_SPACE and hero.hp <= 0:
					done = False
					key_space = True


			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_1:
					key1 = True
				if e.key == pygame.K_2:
					key2 = True
				if e.key == pygame.K_3:
					key3 = True
				if e.key == pygame.K_e:
					key_ent = True
				if e.key == pygame.K_q:
					key_q = True					
				if e.key == pygame.K_w:
					key_w = True

			if e.type == pygame.KEYUP:
				if e.key == pygame.K_1:
					key1 = False
				if e.key == pygame.K_2:
					key2 = False
				if e.key == pygame.K_3:
					key3 = False
				if e.key == pygame.K_e:
					key_ent = False						
				if e.key == pygame.K_q:
					key_q = False
				if e.key == pygame.K_w:
					key_w = False					


	if key_q and hppotionnum >0 and hero.hp > 0:
		hppotionnum = hppotionnum - 1
		bottle_random = random.randint (1,6)
		hero.hp = hero.hp + bottle_random


	
		#stroke12_red = '+ ' + str(bottle_random)+ ' hp'
		#stroke11 = ''
		key_q = False
		#stopshow = False
		#time_sec = 0
		#time = 0

	hero.update (left, right, blocks, monsters)
	bg.fill ((black))





	time_sec = int(time/2)
	time_sec_m = int(time_m/2)
	time = time + 1	
	time_m = time_m + 1	
	if time_sec_m > 100:

		stopshow_m = True
		time_sec_m = 0
		time_m = 0

	if time_sec > 100:
		stopshow = True

		time_sec = 0
		time = 0

	if special_wiz == True:
		wiz_conversation ()


	if hero.hp <= 0 and battle_mode == False:
		clear_talk ()
		talks (1, 'Вы умерли.')
		talks (2,'Никто не вспомнит о вас,')
		talks (3, 'погребенном в пучине забвения.')
		talks (5, 'GAME OVER')
		talks (8, 'SPACE')
		pygame.sprite.Sprite.kill (hero)
		battle_mode = False
		move = False



	quest ()
	b.draw (bg)
	a_group.draw (bg)

	hp_modify ()
	if battle_mode == True:
		battle (hero, current_monster)	
	
	window.blit(start_screen, (10, 10))
	start_screen.fill ((black))
	window.blit(bg, (10, 40))
	window.blit(bg2, (620, 40))
	window.blit(bg4_text, (10, 450))
	bg4_text.fill ((black))
	bg4_text.blit (life, (25,130+(-10*hero.hp)))
	bg4_text.blit (life_black, (25,130))

	bg4_text.blit (mana, (5,130+(-10*hero.mp)))
	bg4_text.blit (mana_black, (5,130))	
	mana.fill (blue)
	life.fill (red)
	life_black.fill (black)
	mana_black.fill (black)
	bg2.blit (bg3, (10,10))
	bg3.fill ((0,0,0))




	if monster_info == True:
		bg4_text.blit (bg5, (625,10) )
		#bg5.blit (skel_info, (0,0))
		bg5.fill ((80,100,200))
		bg5.blit(inf_font.render (minfo1,True, (250,250,250)), (10,10))
		bg5.blit(inf_font.render (minfo2,True, (250,250,250)), (10,30))
		bg5.blit(inf_font.render (minfo3,True, (250,250,250)), (10,50))
		bg5.blit(inf_font.render (minfo4,True, (250,250,250)), (10,70))
		bg5.blit(inf_font.render (minfo5,True, (250,250,250)), (95,30))

	bg3.blit(inf_font.render (stroke1, True, (250,250,250)), (15,0))
	bg3.blit(inf_font.render (stroke2, True, (250,250,250)), (15,30))
	bg3.blit(inf_font.render (stroke3, True, (250,250,250)), (15,60))
	bg3.blit(inf_font.render (stroke4, True, (250,250,250)), (15,90))
	bg3.blit(inf_font.render (stroke5, True, (250,250,250)), (15,120))
	bg3.blit(inf_font.render (stroke6, True, (250,250,250)), (15,150))
	bg3.blit(inf_font.render (stroke7, True, (250,250,250)), (15,180))
	bg3.blit(inf_font.render (stroke8, True, (250,250,250)), (15,210))
	bg3.blit(inf_font.render (stroke9, True, (250,250,250)), (15,240))
	bg3.blit(inf_font.render (stroke10, True, (250,250,250)), (15,270))
	bg3.blit(inf_font.render (stroke11, True, (250,250,250)), (15,300))
	bg3.blit(inf_font.render (stroke12, True, (250,250,250)), (15,330))
	bg3.blit(inf_font.render (stroke13, True, (250,250,250)), (15,350))

	#bg3.blit(inf_font.render (str(stroke12_red), True, (red)), (15,330))

	bg4_text.blit(inf_font.render (tst1, True, (250,250,250)), (50,10))
	bg4_text.blit(inf_font.render (tst2, True, (250,250,250)), (50,30))
	bg4_text.blit(inf_font.render (tst3, True, (250,250,250)), (50,50))
	bg4_text.blit(inf_font.render (tst4, True, (250,250,250)), (50,70))
	bg4_text.blit(inf_font.render (tst5,True, (250,250,250)), (50,90))
	bg4_text.blit(inf_font.render (tst6,True, (250,250,250)), (50,110))
	bg4_text.blit(inf_font.render (tst7,True, (250,250,250)), (50,130))

	bg4_text.blit(inf_font.render (tst6_red,True, (red)), (50,110))
	bg4_text.blit(inf_font2.render (tst7_back,True, (red)), (500,130))

	life_black.blit(inf_font2.render (str(hero.hp), True, (225,225,225)), (2,0))
	mana_black.blit(inf_font2.render (str(hero.mp), True, (225,225,225)), (2,0))

	
	if makepause:

		if key_ent:
			key_ent = False
			move = True
			makepause = False




	pygame.display.update() 
	
	timer.tick (35)



end_title.main ()