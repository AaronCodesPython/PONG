import pygame
import numpy as np


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # Player and Ball
        self.p1_pos = np.array([10, 250])
        self.p2_pos = np.array([780, 250])
        self.ball_pos = np.array([385, 285])

        # movement
        self.ball_acceleration = np.array([5, 1])
        self.player_acceleration = np.array([0, 4])

        self.game_loop()

    def reset(self):
        self.p1_pos = np.array([10, 250])
        self.p2_pos = np.array([780, 250])
        self.ball_pos = np.array([385, 285])

    def game_loop(self):
        run = True
        while run:
            # FPS Limit
            self.clock.tick(60)
            self.screen.fill([0, 0, 0])

            self.input()
            self.draw()
            self.update()

            pygame.display.flip()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if pygame.key.get_pressed()[pygame.K_w]:
            self.p1_pos += self.player_acceleration * np.array([0, -1])

        if pygame.key.get_pressed()[pygame.K_s]:
            self.p1_pos += self.player_acceleration

    def draw(self):
        # Drawing Player and Ball on Window
        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), (self.p1_pos[0], self.p1_pos[1], 10, 200))
        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), (self.p2_pos[0], self.p2_pos[1], 10, 200))
        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), (self.ball_pos[0], self.ball_pos[1], 15, 15))

    def update(self):
        if self.ball_screen_collision_left() or self.ball_screen_collision_right():
            self.reset()

        if self.ball_p_collision():
            self.ball_acceleration = self.ball_acceleration * np.array([1, 1])

        if self.ball_screen_collision_bottem() or self.ball_screen_collision_top():
            self.ball_acceleration = self.ball_acceleration * np.array([1, -1])

        self.ball_pos += self.ball_acceleration

    # checks if ball hit player
    def ball_p_collision(self):
        return self.ball_p1_collision() or self.ball_p2_collision()

    # check if ball hits player or edge of screen
    def ball_p1_collision(self):
        return self.aabb_col(self.p1_pos[0], self.p1_pos[1], 10, 100, self.ball_pos[0], self.ball_pos[1], 15, 15)

    def ball_p2_collision(self):
        return self.aabb_col(self.p2_pos[0], self.p2_pos[1], 10, 100, self.ball_pos[0], self.ball_pos[1], 15, 15)

    def ball_screen_collision_left(self):
        return self.ball_pos[0] <= 0

    def ball_screen_collision_top(self):
        return self.ball_pos[1] >= 0

    def ball_screen_collision_right(self):
        return self.ball_pos[0] + 15 >= 800

    def ball_screen_collision_bottem(self):
        return self.ball_pos[1] + 15 >= 600

    # Hitboxes
    def aabb_col(self, a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
        collision_x = a_x + a_width >= b_x and b_x + b_width >= a_x
        collision_y = a_y + a_height >= b_y and b_y + b_height >= a_y

        return collision_x, collision_y


Game()
