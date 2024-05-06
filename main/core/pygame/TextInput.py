import pygame

pygame.init()
class TextInput():
    def __init__(self, rect = pygame.Rect(0, 0, 90, 32), char_limit = 6, editable = True, font = pygame.font.Font(None, 30), text = '', activecolor = pygame.Color(0,0,0,10), passivecolor = pygame.Color(0,0,0,0)):
        self.font = font
        self.rect = rect
        self.char_limit = char_limit
        self.text = text
        self.activecolor = activecolor
        self.passivecolor = passivecolor
        self.color = passivecolor
        self.active = False
        self.editable = editable

    def observeClick(self, event):
        if self.editable:
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

    def draw(self, screen, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        show = self.text
        if len(self.text) > self.char_limit:
            show = self.text[-self.char_limit:]
        text_surface = self.font.render(show, False, (0,0,0))

        screen.blit(surface, (0,0))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 4*((self.rect.h - 24)//8+1)))
        
    def drawList(self, screen, surface,  stringList):
        pygame.draw.rect(surface, self.color, self.rect)
        screen.blit(surface, (0,0))
        for i in range(len(stringList)):
            text_surface = self.font.render(stringList[i], False, (0,0,0))
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 4*(i*5)))

    def drawList(self, screen, surface, stringList):
        pygame.draw.rect(surface, self.color, self.rect)
        screen.blit(surface, (0,0))
        for i in range(len(stringList)):
            text_surface = self.font.render(stringList[i], False, (0,0,0))
            screen.blit(text_surface, (self.rect.x+5, self.rect.y + 4*(i*5)))

    def getText(self) -> str:
        return self.text

    def setText(self, text):
        self.text = text

    def setEditable(self, boolean):
        self.editable = boolean

    def setActive(self, boolean):
        self.color = self.passivecolor
        self.active = boolean