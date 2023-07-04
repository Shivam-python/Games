import pygame, random, sys, time


class Game:
    def __init__(self) -> None:
        # initializing pygame
        pygame.init()
        
        # window size
        self.frame_size_x = 720
        self.frame_size_y = 480

        # initializing colors 
        self.GREEN = pygame.Color(0, 255, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.BLACK = pygame.Color(0, 0, 0)
        self.RED = pygame.Color(255,0,0)

        # Initialise game window
        pygame.display.set_caption('Snake Eater Game')
        self.screen = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))

        # FPS (frames per second) controller
        self.fps_controller = pygame.time.Clock()
        
        # making screen BLACK
        self.screen.fill(self.BLACK)


        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]


        self.food_pos = [random.randrange(1, (self.frame_size_x//10)) * 10, random.randrange(1, (self.frame_size_y//10)) * 10]
        self.food_spawn = True

        # start direction
        self.direction = 'RIGHT'

        # deciding which direction to change the snake
        self.change_to = self.direction

        self.score = 0

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_screen = my_font.render('YOU DIED', True, self.RED)
        game_over_rectangle = game_over_screen.get_rect()
        game_over_rectangle.midtop = (self.frame_size_x/2, self.frame_size_y/4)
        self.screen.fill(self.BLACK)
        self.screen.blit(game_over_screen, game_over_rectangle)

        # showing score in the enf screen
        self.show_score(0, self.RED, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    # Score
    def show_score(self,choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (self.frame_size_x/10, 15)
        else:
            score_rect.midtop = (self.frame_size_x/2, self.frame_size_y/1.25)
        self.screen.blit(score_surface, score_rect)


    def update_snake_position(self):
        # Making sure the snake cannot move in the opposite direction instantaneously
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Moving the snake
        if self.direction == 'UP':
            self.snake_pos[1] -= 10
        if self.direction == 'DOWN':
            self.snake_pos[1] += 10
        if self.direction == 'LEFT':
            self.snake_pos[0] -= 10
        if self.direction == 'RIGHT':
            self.snake_pos[0] += 10
    
    def check_game_over(self):
        
        # Getting out of bounds
        game_over = False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x-10:
            game_over = True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y-10:
            game_over = True
        
        # Touching the snake body
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                game_over = True
        return game_over

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                    
                    # canging directions on key pressed
                    if event.key == pygame.K_UP:
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        self.change_to = 'RIGHT'


            self.update_snake_position()

            # Snake body growing mechanism
            self.snake_body.insert(0, list(self.snake_pos))
            if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
                self.score+=1
                self.food_spawn = False
            else:
                self.snake_body.pop()

            # Spawning food on the screen
            if not self.food_spawn:
                self.food_pos = [random.randrange(1, (self.frame_size_x//10)) * 10, random.randrange(1, (self.frame_size_y//10)) * 10]
            self.food_spawn = True

            self.screen.fill(self.BLACK)
            
            # Snake body
            for pos in self.snake_body:
                pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

            # Snake food
            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))

            
            if self.check_game_over():
                self.game_over()

            self.show_score(1, self.WHITE, 'consolas', 20)
            # Refresh game screen
            pygame.display.update()
            
            # Refresh rate
            self.fps_controller.tick(10)


if __name__ == '__main__':
    game = Game()
    game.run()