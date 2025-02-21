from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_png