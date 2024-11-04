from settings import *
from sys import exit
from os.path import join

# components
from game import Game
from score import Score
from preview import Preview

from random import choice

class Main:
    def __init__(self):
        # general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

        # components
        self.score = Score()
        self.preview = Preview()
        self.start_new_game()

        # audio 
        self.music = pygame.mixer.Sound(join('Tetris', 'sound', 'music.wav'))
        self.music.set_volume(0.05)
        self.music.play(-1)

    def start_new_game(self):
        """Start a new game and reset necessary components."""
        self.game = Game(self.get_next_shape, self.update_score)
        self.next_shapes = [choice(list(TETROMINOS.keys())) for _ in range(3)]

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Restart game on key press after game over
                if self.game.game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Restart the game with SPACE key
                        self.start_new_game()

            # display 
            self.display_surface.fill(GRAY)
            
            # components
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            # updating the game
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
