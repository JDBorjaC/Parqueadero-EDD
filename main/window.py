import datetime

from core.parqueadero.Parqueadero import Parqueadero
from core.parqueadero.vehiculos.TipoVehiculo import TipoVehiculo
from core.pygame.Button import Button
from core.pygame.Image import Image

import pygame

from main.core.pygame.TextInput import TextInput

#display stuff
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1000

#setup---------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption('IpePark')
pygame.display.set_icon(pygame.image.load('core/assets/sosio.png'))
colorAvailable = pygame.Color(125, 158, 125)
colorUnavailable = pygame.Color(237, 71, 71)

parqueadero = Parqueadero()

#Listas de imagenes a mostrar
tab1 = []
tab2 = []
tab3 = []

#Listas de TextInput
tab2inputs = {
    'lot': TextInput(pygame.Rect(135,38,90,32), 6, False),
    'placa': TextInput(pygame.Rect(191,90,85,24), 6),
    'tipo': TextInput(pygame.Rect(191,152,90,32), 6, False),
    'estado': TextInput(pygame.Rect(191,222,90,32), 6, False),
    'response': TextInput(pygame.Rect(70,340,200,32), 50,False)
}
tab3inputs = {
    'placa': TextInput(pygame.Rect(163,157,267,44)),
    'piso': TextInput(pygame.Rect(163,335,267,44))
}

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
deleteBtnImg = pygame.image.load('core/assets/deleteBtn.png').convert_alpha()
deleteBtnImgPressed = pygame.image.load('core/assets/deleteBtnPressed.png').convert_alpha()
        

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
deleteBtn = Button(99+69, 342+16, deleteBtnImg, deleteBtnImgPressed, screen)


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
    
    piso = parqueadero.getFloor(floor)
    xPixel = -1
    yOffset = 0
    for j in range(0, 21):
                    
        slot = piso.getSlotByName(chr(65+i)+str(j+1))
        
        #Decide image
        match slot.getType():
            case TipoVehiculo.car:
                pArray = pygame.PixelArray(carLotImg)                    
            case TipoVehiculo.motorcycle:
                pArray = pygame.PixelArray(bikeLotImg)
            case TipoVehiculo.reduced_mobility:
                pArray = pygame.PixelArray(discLotImg)
                
        
        #Decide color
        if slot.keyEquals(currentSlot):
            pArray.replace(pygame.Color(255,0,161,), pygame.Color(100,0,255))
        elif not slot.getVehicle(): #If there *is* a vehicle in the slot, paint it green
            pArray.replace(pygame.Color(255, 0, 161), colorAvailable)
        else: #else, paint it red
            pArray.replace(pygame.Color(255, 0, 161), colorUnavailable)
        
        yOffset = yOffset + 1 if xPixel == 6 else yOffset
        xPixel = xPixel + 1 if xPixel < 6 else 0
        
        #comienzas en 381, 42
        #una fila mide 560 pixeles
        #a 381 le sumas la fraccion de la longitud en la que estas (1/7, 2/7, 3/7...)
        currentLot = pArray.make_surface()
        #Reset pArray
        pArray.replace(pygame.Color(100,0,255), pygame.Color(255,0,161))
        pArray.replace(colorAvailable, pygame.Color(255,0,161))
        pArray.replace(colorUnavailable, pygame.Color(255, 0, 161))
        screen.blit(currentLot, (381+(xPixel/7)*560, 30+(160*yOffset)))

def resetLabelsTab2():
    tab2inputs['lot'].setText('')
    tab2inputs['tipo'].setText('')
    tab2inputs['estado'].setText('')


#game loop
run = True
tab = 0
floor = 0
row = 0
current_col = -1
currentSlot = ''
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
                currentSlot = ''
                resetLabelsTab2()

            if floorDownBtn.draw() and floor>0:   
                floor -= 1
                currentSlot = ''
                resetLabelsTab2()
            
            if rowUpBtn.draw() and row<9:
                row += 1
                currentSlot = ''
                resetLabelsTab2()
            
            if rowDownBtn.draw() and row>0:
                row -= 1
                currentSlot = ''
                resetLabelsTab2()
                
            if deleteBtn.draw():
                print("delete btn pressed")
            
            if addBtn.draw():
                
                flag = True
                msg = ''
                placa = tab2inputs['placa'].getText()

                if len(placa) != 6:
                    flag = False
                    msg = 'La placa debe contener 6 caracteres'
                elif not (placa[:3].isalpha() and placa[3:].isdigit()):
                    flag = False
                    msg = 'La placa ingresada no es válida'
                elif parqueadero.vehicles.getBy(placa.upper()):
                    flag = False
                    msg = 'El vehículo ya se encuentra en un puesto'

                if flag:
                    msg = 'Se agregó el vehículo con éxito'
                    parqueadero.addVehicle(floor, currentSlot, placa, datetime.time)

                tab2inputs['response'].setText(msg)

            renderLotButtons(floor, row)
            for textinput in tab2inputs.values():
                textinput.draw(screen, surface)
        
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

            for textinput in tab3inputs.values():
                textinput.draw(screen, surface)
    
    #Events
    for event in pygame.event.get():
        #Quitting
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if tab == 1:
                if current_col != -1:
                    currentSlot = chr(65+row) + str(current_col)
                    slot = parqueadero.getFloor(floor).getSlotByName(currentSlot)
                    tab2inputs['lot'].setText(slot.getName())
                    vtype = ""
                    match slot.getType():
                        case TipoVehiculo.car:
                            vtype = "Car"
                        case TipoVehiculo.motorcycle:
                            vtype = "Bike"
                        case TipoVehiculo.reduced_mobility:
                            vtype = "Disc."
                    tab2inputs['tipo'].setText(vtype)
                    estado = slot.getEstado()
                    tab2inputs['estado'].setText(estado)
                    if estado == 'Ocupado':
                        tab2inputs['placa'].setEditable(False)
                    else:
                        tab2inputs['placa'].setEditable(True)

                for textinput in tab2inputs.values():
                    textinput.observeClick(event)
            elif tab == 2:
                for textinput in tab3inputs.values():
                    textinput.observeClick(event)

        if event.type == pygame.KEYDOWN:
            if tab == 1:
                for textinput in tab2inputs.values():
                    textinput.handleTyping(event)
            elif tab == 2:
                for textinput in tab3inputs.values():
                    textinput.handleTyping(event)

    pygame.display.update()

pygame.quit()
