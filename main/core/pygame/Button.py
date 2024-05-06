import pygame
class Button():
    def __init__(self, x, y, image, hoverImage, screen):
        self.image = image
        self.hoverImage = hoverImage
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-(self.image.get_width()/2), y-(self.image.get_height()/2))
        self.clicked = False
        
        self.screen = screen
        
    def draw(self) -> bool:
        
        action = False
        img = self.image
        
        #get mousepos
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            img = self.hoverImage
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False                
        
        self.screen.blit(img, (self.rect.x, self.rect.y))
        
        return action