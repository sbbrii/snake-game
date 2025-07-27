import pygame,sys, random
from pygame.math import Vector2

pygame.init()

title_font = pygame.font.Font(None,60)
score_font = pygame.font.Font(None, 40)

GREY = (32,32,32)
GREEN = (0,255,0)

cell_size = 30
no_cells = 25

OFFSET = 75

class Foods:
    def __init__(self,snake_body):
         self.pos = self.random_food(snake_body)

    def draw(self):
        food_rect = pygame.Rect(OFFSET+self.pos.x * cell_size,OFFSET+self.pos.y * cell_size,cell_size,cell_size)
        scr.blit(food_pic,food_rect)

    def gen_food(self):
        x = random.randint(1,no_cells-1)
        y = random.randint(1,no_cells-1)
        return Vector2(x,y) 


    def random_food(self,snake_body):
        pos = self.gen_food()

        while pos in snake_body:
            pos = self.gen_food()
        
        return pos


class Snake:
    def __init__(self):
        self.body = [Vector2(6,9),Vector2(5,9),Vector2(4,9)]
        self.dir = Vector2(1,0)
        self.add_segment = False
    def draw(self):
        for square in self.body:
            square_draw = (OFFSET+square.x * cell_size,OFFSET+square.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(scr,GREEN,square_draw,0,7)

    def update(self):
        self.body.insert(0,self.body[0]+self.dir)
        if self.add_segment == True:
            self.add_segment = False
        else: 
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6,9),Vector2(5,9),Vector2(4,9)]
        self.dir = Vector2(1,0)       

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Foods(self.snake.body)
        self.state = "Running"
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw() 
    def update(self):
        if self.state=="Running":
            self.snake.update()
            self.snake_eat_food()
            self.snake_hit_edge()
            self.snake_eat_tail()

    def snake_eat_food(self):
        if self.food.pos == self.snake.body[0]:
            self.food.pos = self.food.random_food(self.snake.body)
            self.snake.add_segment = True
            self.score+=1

    def snake_hit_edge(self):
            if self.snake.body[0].x == no_cells or self.snake.body[0].x ==-1:
                self.game_over()
            if self.snake.body[0].y == no_cells or self.snake.body[0].y ==-1:
                self.game_over()
    def snake_eat_tail(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()
    def game_over(self):
        self.snake.reset()
        self.food.random_food(self.snake.body)
        self.state = "Stopped"
        self.score = 0


scr = pygame.display.set_mode((2*OFFSET+cell_size*no_cells, 2*OFFSET+cell_size*no_cells))

pygame.display.set_caption("Snake game")

clk = pygame.time.Clock()

food_pic = pygame.image.load("Items/apple.png")


game = Game()

SNAKE_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE,200)


while True:
    for event in pygame.event.get():
        if event.type==SNAKE_UPDATE:
            game.update()
        if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type==pygame.KEYDOWN:
                if game.state=="Stopped":
                    game.state="Running"

                if event.key == pygame.K_w and game.snake.dir != Vector2(0,1):
                    game.snake.dir = Vector2(0,-1)
                if event.key == pygame.K_s and game.snake.dir != Vector2(0,-1):
                    game.snake.dir = Vector2(0,1)
                if event.key == pygame.K_d and game.snake.dir != Vector2(-1,0):
                    game.snake.dir = Vector2(1,0)
                if event.key == pygame.K_a and game.snake.dir != Vector2(1,0):
                    game.snake.dir = Vector2(-1,0)

    #draw
    scr.fill(GREY)
    pygame.draw.rect(scr,GREEN,
                     (OFFSET-5, OFFSET-5, cell_size*no_cells+10, cell_size*no_cells+10),5)

    game.draw()
    title_surface = title_font.render("Retro Snake",True,GREEN)
    scr.blit(title_surface,(OFFSET-5, 10))
    score_surface = score_font.render(str(game.score),True,GREEN)
    scr.blit(score_surface,(OFFSET-5, OFFSET+cell_size*no_cells+10))
    pygame.display.update()
    clk.tick(60)
