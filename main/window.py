from core.parqueadero.Parqueadero import Parqueadero
from core.pygame.Button import Button
from core.pygame.Image import Image

import pygame

from main.core.pygame.TextInput import TextInput

#display stuff
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1000

#setup---------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Demo')
colorAvailable = pygame.Color(125, 158, 125)
colorUnavailable = pygame.Color(237, 71, 71)

parqueadero = Parqueadero()

#Listas de imagenes a mostrar
tab1 = []
tab2 = []

<<<<<<< Updated upstream
=======
#Listas de TextInput
tab2inputs = {
    'placa': TextInput(pygame.Rect(191,82,90,32)),
    'tipo': TextInput(pygame.Rect(191,152,90,32)),
    'estado': TextInput(pygame.Rect(191,222,90,32))
}
tab3inputs = []

#Surfaces que se van a usar
>>>>>>> Stashed changes
titleImg = pygame.image.load('core/assets/title.png').convert_alpha()
backdropImg = pygame.image.load('core/assets/menuBackdrop.png').convert_alpha()
startBtnImg = pygame.image.load('core/assets/startButtonN.png').convert_alpha()
startBtnHov = pygame.image.load('core/assets/startButtonP.png').convert_alpha()
menuBackground = pygame.image.load('core/assets/menuDrawing.png').convert_alpha()
parkgridImg = pygame.image.load('core/assets/windowref.png').convert_alpha()

carLotImg = pygame.image.load('core/assets/carlot.png').convert_alpha()
        

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
def renderLotButtons(floor):
    
    floor = parqueadero.getFloor(floor)
    
    for i in range(0, 10):
        for j in range(0, 21):
                        
            slot = floor.getSlotByName(chr(65+i)+str(j+1))
            pArray = pygame.PixelArray(carLotImg)
            if not slot.getVehicle(): #If there *is* a vehicle in the slot, paint it green
                pArray.replace(pygame.Color(255, 0, 161), colorAvailable)
            else: #else, paint it red
                pArray.replace(pygame.Color(255, 0, 161), colorUnavailable)
            
            currentLot = pArray.make_surface()
            screen.blit(currentLot, (j*30+347, i*44+27))


#game loop
framecount = 0
run = True
tab = 0;
while run:

    framecount += 1
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

            mouse_pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = mouse_pos
            if framecount % 600 == 0:
                if 347 < mouse_x < SCREEN_WIDTH and 27 < mouse_y < SCREEN_WIDTH:
                    current_col = int((mouse_x - 347)/30)+1
                    current_row = chr(65 + int((mouse_y - 27)/44))
                    print("currently at "+current_row+str(current_col))
                else:
                    print("currently nowhere")
            
            #Images
            for img in tab2:
                img.render()
            
            
<<<<<<< Updated upstream
            floor = 1
            renderLotButtons(floor)
=======
            if rowUpBtn.draw() and row<9:
                row += 1
            
            if rowDownBtn.draw() and row>0:
                row -= 1
                        
            renderLotButtons(floor, row)
            for textinput in tab2inputs.values():
                textinput.draw(screen)
>>>>>>> Stashed changes
    
    #Events
    for event in pygame.event.get():
        #Quitting
        if event.type == pygame.QUIT:
            run = False
<<<<<<< Updated upstream
    
=======
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tab == 1:
                if current_col != -1:
                    print("currently at ", chr(65+row), current_col)
                for textinput in tab2inputs.values():
                    textinput.observeClick(event)

        if event.type == pygame.KEYDOWN:
            if tab == 1:
                for textinput in tab2inputs.values():
                    textinput.handleTyping(event)


>>>>>>> Stashed changes
    pygame.display.update()

pygame.quit()