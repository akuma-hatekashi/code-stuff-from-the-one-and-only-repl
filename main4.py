from turtle import *
from random import randint as rr, choice as rc
from time import sleep as ts

wn = Screen()
wn.bgcolor('black')

death_list = []

points = 0

pen_down = False
colorss = False

player = Turtle()
player.ht()
player.color('blue')
player.up()
player.speed(2)
player.shape('turtle')

goal = Turtle()
goal.ht()
goal.speed(0)
goal.up()
goal.goto(200, 0)
goal.color('green')
goal.shape('circle')

border = Turtle()
border.speed(0)
border.up()
border.color('yellow')
border.shape('circle')
border.goto(-300, -300)
border.pensize(3)
border.down()
border.goto(-300, 300)
border.goto(300, 300)
border.goto(300, -300)
border.goto(-300, -300)
border.ht()

def pen():
	global player
	global pen_down

	if pen_down == False:
		pen_down = True
		player.down()
	
	elif pen_down == True:
		pen_down = False
		player.up()
		player.clear()

def colorswaper():
	global player
	global colorss

	colors = ['red', 'blue', 'purple', 'yellow', 'magenta', 'green', 'lime', 'lightblue', 'pink', ]
	player.color(rc(colors))

def deathh(points):
	player.speed(0)
	bye()
	print('score:', points)
	quit()

def create_new_death(death_list, player, goal):
	new_death = Turtle()
	new_death.up()
	new_death.speed(0)
	new_death.color('red')
	new_death.shape('circle')
	new_death.goto(rr(-200, 200), rr(-200, 200))

	while True:
		if player.distance(new_death) < 10:
			new_death.goto(rr(-400, 400), rr(-200, 200))
		
		elif goal.distance(new_death) < 20:
			new_death.goto(rr(-400, 400), rr(-200, 200))
		
		else:
			break
	
	death_list.append(new_death)

def score(goal, death_list, player):
	global points
	points += 1
	goal.goto(rr(-200, 200), rr(-200, 200))

	create_new_death(death_list, player, goal)

def checker(death, player, goal):
	if goal.distance(player) < 15:
		score(goal, death_list, player)
	
	for death in death_list:
		if player.distance(death) < 8:
			deathh(points)
	
	if player.xcor() > 300:
		player.speed(0)
		player.setheading(180)
		player.speed(2)
	
	elif player.xcor() < -300:
		player.speed(0)
		player.setheading(0)
		player.speed(2)
	
	elif player.ycor() > 300:
		player.speed(0)
		player.setheading(270)
		player.speed(2)
	
	elif player.ycor() < -300:
		player.speed(0)
		player.seth(90)
		player.speed(2)

def left_turn():
	global player
	player.speed(0)
	player.left(90)
	player.speed(2)

def right_turn():
	global player
	player.speed(0)
	player.right(90)
	player.speed(2)



wn.onkey('a', left_turn)
wn.onkey('d', right_turn)
wn.onkey('f', pen)
wn.onkey('z', colorswaper)
wn.listen()
player.st()
goal.st()

while True:
	player.forward(5)
	checker(death_list, player, goal)
