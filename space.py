import os
import turtle
import math
import random
import winsound

window = turtle.Screen()
window.title("Space Invaders")
window.bgpic("space1.gif")

turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("laser.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(0,4):
	border_pen.fd(600)
	border_pen.lt(90)

border_pen.hideturtle()	

#enemies

num_of_enemies = 5

enemies = []

for i in range(num_of_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies: 
    
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(0, 200)
    enemy.setposition(x, y)

enemyspeed = 4

#scoring

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-280, 260)
scorestring = "Score : " + str(score)
score_pen.write(scorestring, font = ("Arial", 14, "normal"))
score_pen.hideturtle()

#player

player = turtle.Turtle()
player.color("green")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.lt(90)

#player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("laser.gif")
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.speed(0)
bullet.hideturtle()
bullet.setposition(-310,-310)
bullet.setheading(90)
bulletspeed = 24

bulletstate = "ready"

#player movement
playerspeed = 5

def move_left(event):
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)    


def move_right(event):
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    
    global bulletstate
    
    if bulletstate == "ready":
        
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        #winsound.PlaySound("shoot", winsound.SND_FILENAME)

def isCollision(t1, t2):
    dis = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    
    if dis < 25 :
       return True
    return False    

#binding keys
turtle.listen()
turtle.getcanvas().bind('<Left>', move_left)
turtle.getcanvas().bind('<Right>', move_right)
#turtle.onkey(move_left, "Left")
#turtle.onkey(move_right, "Right")    
turtle.onkey(fire_bullet, "space")

#main loop
while True:
    
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
            
        #move enemy
        
        if enemy.xcor() > 272:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1
        
        if enemy.xcor() < -272 :
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            enemyspeed *= -1
        
        #check for collisions
        if(isCollision(bullet, enemy)):
            
            #winsound.PlaySound("invaderkilled", winsound.SND_FILENAME)
            bullet.hideturtle()
            bullet.setposition(-310, -310)
            bulletstate = "ready"
            x = random.randint(-200, 200)
            y = random.randint(0, 200)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score : " + str(score)
            score_pen.clear()
            score_pen.write(scorestring, font = ("Arial", 14, "normal"))
            
        if (isCollision(player, enemy) or (enemy.ycor() <= player.ycor())):
        
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
            bullet.hideturtle()
            print("Game Over")

            score_pen1 = turtle.Turtle()
            score_pen1.speed(0)
            score_pen1.color("white")
            score_pen1.penup()
            score_pen1.setposition(-160, 0)
            scorestring1 = "GAME  OVER"
            score_pen1.write(scorestring1, font = ("Arial", 40, "normal"))
            score_pen1.hideturtle()

            break            
        
    #move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 280:
        bulletstate = "ready"
        bullet.hideturtle()

    
        




turtle.done()