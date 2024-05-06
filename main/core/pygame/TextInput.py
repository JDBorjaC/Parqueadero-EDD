import pygame

pygame.init()
class TextInput():
    def __init__(self, rect = pygame.Rect(0, 0, 90, 32), text = '', font = pygame.font.Font(None, 32), activecolor = pygame.Color('lightskyblue3'), passivecolor = pygame.Color('chartreuse4')):
        self.font = font
        self.rect = rect
        self.text = text
        self.activecolor = activecolor
        self.passivecolor = passivecolor
        self.color = passivecolor
        self.active = False

    def observeClick(self, event):
        if self.rect.collidepoint(event.pos):
            self.active = True
            self.color = self.activecolor
        else:
            self.active = False
            self.color = self.passivecolor

    def handleTyping(self, event):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        sexo = self.text
        if len(self.text) > 6:
            sexo = self.text[-6:]
        text_surface = self.font.render(sexo, False, (255, 255, 255))

        #text_surface.set_clip(self.rect)
        # render at position stated in arguments
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))