from core.parqueadero.Parqueadero import Parqueadero
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

rightArrImg = pygame.image.load('core/assets/arrow.png').convert_alpha()
leftArrImg = pygame.transform.flip(rightArrImg, True, False)
rightArrPressedImg = pygame.image.load('core/assets/pressedarrow.png').convert_alpha()
leftArrPressedImg = pygame.transform.flip(rightArrPressedImg, True, False)

rightSkinnyImg = pygame.image.load('core/assets/skinnyarrow.png').convert_alpha()
leftSkinnyImg = pygame.transform.flip(rightSkinnyImg, True, False)
rightSkinnyPressed = pygame.image.load('core/assets/skinnypressed.png').convert_alpha()
leftSkinnyPressed = pygame.transform.flip(rightSkinnyPressed, True, False)
        

#instance buttons
startBtn = Button(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-75, startBtnImg, startBtnHov, screen)
floorUpBtn = Button(190+36, 424+33, rightArrImg, rightArrPressedImg, screen)
floorDownBtn = Button(98+36, 424+33, leftArrImg, leftArrPressedImg, screen)
rowUpBtn = Button(704+58, 461+13, rightSkinnyImg, rightSkinnyPressed, screen)
rowDownBtn =Button(497+58, 461+13, leftSkinnyImg, leftSkinnyPressed, screen)


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

#la fila a mostrar se toma como parametro i, junto con el floor
def renderLotButtons(floor, i):
    
    floor = parqueadero.getFloor(floor)
    xPixel = -1
    yOffset = 0
    for j in range(0, 21):
                    
        slot = floor.getSlotByName(chr(65+i)+str(j+1))
        
        #Decide image
        match slot.getKind():
            case "car":
                pArray = pygame.PixelArray(carLotImg)                    
            case "motorcycle":
                pArray = pygame.PixelArray(bikeLotImg)
            case "reduced_mobility":
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
                
            if floorUpBtn.draw() and floor<2:
                floor += 1
            
            if floorDownBtn.draw() and floor>0:   
                floor -= 1
            
            if rowUpBtn.draw() and row<9:
                row += 1
            
            if rowDownBtn.draw() and row>0:
                row -= 1
            
            print("floor: ",floor," row: ",row)
            
            renderLotButtons(floor, row)
    
    #Events
    for event in pygame.event.get():
        #Quitting
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()