import pgzrun
import random
WIDTH = 1200
HEIGHT = 1000
ship = Actor("ship")
ship.x = 600
ship.y = 950
score = 0
gameover = False
bullets = []
enemys = []
for i in range(10):
    enemys.append(Actor("bee")) 
    enemys[-1].x = random.randint(40,WIDTH-40)
    enemys[-1].y = -100
def draw():
    screen.clear()
    screen.fill("black")
    ship.draw()
    if gameover == True:
        screen.clear()
        screen.fill("red")
        screen.draw.text("GAME OVER",center = (600,500),fontsize = 260)
        screen.draw.text("you killed "+str(score)+" bees out of 10 bees",center = (600,650),fontsize = 100)
        
    for bullet in bullets:
        bullet.draw()
    for enemy in enemys:
        enemy.draw()
def update():
    global gameover,score
    if keyboard.a:
        ship.x = ship.x - 10
    if keyboard.d:
        ship.x = ship.x + 10 
    for bullet in bullets:
        bullet.y = bullet.y - 10
    for enemy in enemys:
        enemy.y = enemy.y +2
        if enemy.y>950:
            gameover = True
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemys.remove(enemy)
                score = score + 1
    

def on_key_down(key):
    if key == key.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y
pgzrun.go()