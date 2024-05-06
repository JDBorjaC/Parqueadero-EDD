import pygame
class Image():
    def __init__(self, x, y, image, screen) -> None:
        self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-(self.image.get_width()/2), y-(self.image.get_height()/2))
        
        self.screen = screen
    
    def render(self) -> None:
        self.screen.blit(self.image, (self.rect.x, self.rect.y))