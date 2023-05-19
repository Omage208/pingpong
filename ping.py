from pygame import *

window = display.set_mode((700, 500))
win_width = 700
win_height = 500
display.set_caption('Ping - Pong')
background = transform.scale(image.load('fon.jpg') , (700, 500))
clock = time.Clock()

img_ball = 'ball.jpg'
img_platform = 'platform.jpg'
recket_x = 200
recket_y = 330


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

for i in range(3):
    ball = (img_ball, -40, 80, 50)

ball = ('ball.jpg', 160, 200, 50, 50)
platform1 = ('platform1.jpg', 160, 200, 50, 50)
platform2 = ('platform2.jpg', 1950, 450, 50, 50)

finish = False
speed_x = 3
cpeed_y = 3
game = False
while not game:
    for i in event.get():
        if i.type == QUIT:
            game = True
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > win_height - 50:
        or ball.rect.y < 0:
            speed_y *= -1

    if sprite.collide_rect(platorm1, ball):
        or sprite.collide_rect(platform2, ball):
            speed_x *= -1

    if ball.rect.x < 0:
        finish = True

    window.blit(background, (0 ,0))

    display.update()
    clock.tick(50)
