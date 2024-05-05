from Button import Button
from Image import Image

import pygame

#display stuff
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1000

#setup---------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')
colorAvailable = (125, 158, 125)

#Listas de imagenes a mostrar
tab1 = []
tab2 = []

titleImg = pygame.image.load('assets/title.png').convert_alpha()
backdropImg = pygame.image.load('assets/menuBackdrop.png').convert_alpha()
startBtnImg = pygame.image.load('assets/startButtonN.png').convert_alpha()
startBtnHov = pygame.image.load('assets/startButtonP.png').convert_alpha()
menuBackground = pygame.image.load('assets/menuDrawing.png').convert_alpha()
parkgridImg = pygame.image.load('assets/windowref.png').convert_alpha()

carLotImg = pygame.image.load('assets/carlot.png').convert_alpha()
        

#instance buttons
startBtn = Button(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-75, startBtnImg, startBtnHov, screen)

#instance images
menuBackdrop = Image(SCREEN_WIDTH/2, -50, backdropImg, screen)
tab1.append(menuBackdrop)
titleImage = Image(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-180, titleImg, screen)
tab1.append(titleImage)
menubg = Image(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+105, menuBackground, screen)
tab1.append(menubg)
parkgrid = Image(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2), parkgridImg, screen)
tab2.append(parkgrid)

#ir celda por celda y revisar si el lote está ocupado
#dependiendo de eso, sacar un PixelArray del carLotImg, usar PixelArray.replace() para
#reemplazar el color default de magenta con el que viene la imagen al color correspondiente
#luego, blittear el PixelArray a screen.
def renderLotButtons():
    for i in range(0, 10):
        for j in range(0, 21):
            screen.blit(carLotImg, (j*30+347, i*44+27))


#game loop
run = True
tab = 0;
while run:
    
    screen.fill((202, 228, 241))
    
    match tab: #Change buttons and images depending on the tab
        case 0:
            #Images
            for img in tab1:
                img.render()

            #Button stuff
            if startBtn.draw():
                tab = 1
        
        case 1:
            
            #Images
            for img in tab2:
                img.render()
            
            renderLotButtons()
    
    #Events
    for event in pygame.event.get():
        #Quitting
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()