from core.parqueadero.Parqueadero import Parqueadero
from core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo
from core.pygame.Button import Button
from core.pygame.Image import Image

import pygame

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
tab3 = []

#Surfaces que se van a usar
titleImg = pygame.image.load('core/assets/title.png').convert_alpha()
backdropImg = pygame.image.load('core/assets/menuBackdrop.png').convert_alpha()
startBtnImg = pygame.image.load('core/assets/startButtonN.png').convert_alpha()
startBtnHov = pygame.image.load('core/assets/startButtonP.png').convert_alpha()
menuBackground = pygame.image.load('core/assets/menuDrawing.png').convert_alpha()
parkgridImg = pygame.image.load('core/assets/windowref.png').convert_alpha()
carLotImg = pygame.image.load('core/assets/carlot.png').convert_alpha()
bikeLotImg = pygame.image.load('core/assets/bikelot.png').convert_alpha()
discLotImg = pygame.image.load('core/assets/disclot.png').convert_alpha()
addBtnImg = pygame.image.load('core/assets/addBtn.png').convert_alpha()
addBtnPressed = pygame.image.load('core/assets/addBtnPressed.png').convert_alpha()
rightArrImg = pygame.image.load('core/assets/arrow.png').convert_alpha()
leftArrImg = pygame.transform.flip(rightArrImg, True, False)
rightArrPressedImg = pygame.image.load('core/assets/pressedarrow.png').convert_alpha()
leftArrPressedImg = pygame.transform.flip(rightArrPressedImg, True, False)
rightSkinnyImg = pygame.image.load('core/assets/skinnyarrow.png').convert_alpha()
leftSkinnyImg = pygame.transform.flip(rightSkinnyImg, True, False)
rightSkinnyPressed = pygame.image.load('core/assets/skinnypressed.png').convert_alpha()
leftSkinnyPressed = pygame.transform.flip(rightSkinnyPressed, True, False)
tab3refImg = pygame.image.load('core/assets/tab3ref.png').convert_alpha()
searchBtnImg = pygame.image.load('core/assets/searchBtn.png').convert_alpha()
searchBtnPressedImg = pygame.image.load('core/assets/searchBtnPressed.png').convert_alpha()
backwardBtnImg = pygame.image.load('core/assets/backbtn.png').convert_alpha()
backwardBtnPressedImg = pygame.image.load('core/assets/backbtnPressed.png').convert_alpha()
forwardBtnImg = pygame.transform.flip(backwardBtnImg, True, False)
forwardBtnImgPressed = pygame.transform.flip(backwardBtnPressedImg, True, False)
        

#instance buttons
startBtn = Button(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-75, startBtnImg, startBtnHov, screen)
floorUpBtn = Button(178+36, 410+33, rightArrImg, rightArrPressedImg, screen)
floorDownBtn = Button(85+36, 410+33, leftArrImg, leftArrPressedImg, screen)
rowUpBtn = Button(704+58, 445+13, rightSkinnyImg, rightSkinnyPressed, screen)
rowDownBtn = Button(497+58, 445+13, leftSkinnyImg, leftSkinnyPressed, screen)
addBtn = Button(99+69, 270+16, addBtnImg, addBtnPressed, screen)
searchByCarBtn = Button(235+63, 208+24, searchBtnImg, searchBtnPressedImg, screen)
searchFloorBtn = Button(235+63, 386+24, searchBtnImg, searchBtnPressedImg, screen)
forwardBtn = Button(911+44, 425+37, forwardBtnImg, forwardBtnImgPressed, screen)
backwardBtn = Button(4+44, 2+37, backwardBtnImg, backwardBtnPressedImg, screen)


#instance images
menuBackdrop = Image(SCREEN_WIDTH/2, -50, backdropImg, screen)
tab1.append(menuBackdrop)
titleImage = Image(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-180, titleImg, screen)
tab1.append(titleImage)
menubg = Image(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+105, menuBackground, screen)
tab1.append(menubg)
parkgrid = Image(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2), parkgridImg, screen)
tab2.append(parkgrid)
tab3bg = Image(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, tab3refImg, screen)
tab3.append(tab3bg)

#ir celda por celda y revisar si el lote está ocupado
#dependiendo de eso, sacar un PixelArray del carLotImg, usar PixelArray.replace() para
#reemplazar el color default de magenta con el que viene la imagen al color correspondiente
#luego, blittear el PixelArray a screen.

#la fila a mostrar se toma como parametro i, junto con el floor, para colorear cada celda correctamente
def renderLotButtons(floor, i):
    
    floor = parqueadero.getFloor(floor)
    xPixel = -1
    yOffset = 0
    for j in range(0, 21):
                    
        slot = floor.getSlotByName(chr(65+i)+str(j+1))
        
        #Decide image
        match slot.getType():
            case TipoVehiculo.car:
                pArray = pygame.PixelArray(carLotImg)                    
            case TipoVehiculo.motorcycle:
                pArray = pygame.PixelArray(bikeLotImg)
            case TipoVehiculo.reduced_mobility:
                pArray = pygame.PixelArray(discLotImg)
                
        
        #Decide color
        if not slot.getVehicle(): #If there *is* a vehicle in the slot, paint it green
            pArray.replace(pygame.Color(255, 0, 161), colorAvailable)
        else: #else, paint it red
            pArray.replace(pygame.Color(255, 0, 161), colorUnavailable)
        
        yOffset = yOffset + 1 if xPixel == 6 else yOffset
        xPixel = xPixel + 1 if xPixel < 6 else 0
        
        #comienzas en 381, 42
        #una fila mide 560 pixeles
        #a 381 le sumas la fraccion de la longitud en la que estas (1/7, 2/7, 3/7...)
        currentLot = pArray.make_surface()
        screen.blit(currentLot, (381+(xPixel/7)*560, 30+(160*yOffset)))


#game loop
run = True
tab = 0
floor = 0
row = 0
current_col = -1
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
            
            #ubicar la celda a editar en base a la posicion del mouse en vez de usar botones
            mouse_pos = pygame.mouse.get_pos()
            if 381 < mouse_pos[0] < 940:
                if 43 < mouse_pos[1] < 121:#upper sub-row
                    current_col = int((mouse_pos[0] - 381)/80)+1
                elif 202 < mouse_pos[1] < 281: #middle sub-row
                    current_col = int((mouse_pos[0] - 381)/80)+8
                elif 362 < mouse_pos[1] < 441:
                    current_col = int((mouse_pos[0] - 381)/80)+15
                else: #trágico
                    current_col = -1
            else:
                current_col = -1
            
            #Images
            for img in tab2:
                img.render()
                
            #Buttons
            if backwardBtn.draw():
                tab -= 1
            
            if forwardBtn.draw():
                tab += 1
            
            if floorUpBtn.draw() and floor<2:
                floor += 1
            
            if floorDownBtn.draw() and floor>0:   
                floor -= 1
            
            if rowUpBtn.draw() and row<9:
                row += 1
            
            if rowDownBtn.draw() and row>0:
                row -= 1
                
            if addBtn.draw():
                print("addPressed")
                        
            renderLotButtons(floor, row)
        
        case 2:
            
            #Imagenes
            for img in tab3:
                img.render()
            
            #Botones
            if backwardBtn.draw():
                tab -= 1
            
            if searchByCarBtn.draw():
                print("an why he ourple")
            
            if searchFloorBtn.draw():
                print("an whyhe ouprpl")
    
    #Events
    for event in pygame.event.get():
        #Quitting
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tab == 1 and current_col != -1:
                print("currently at ", chr(65+row), current_col)
    
    pygame.display.update()

pygame.quit()