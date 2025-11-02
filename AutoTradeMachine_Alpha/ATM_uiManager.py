import tkinter
import os
from PIL import Image, ImageTk

"""
NAVIGATION ADDRESSES (Right Most Digit Indicated Development Mode (0: Development Mode Does Not Exist, 1: False, 2: True))
    INITIALIZATION PAGE : 00 00 00 00 00
    MAIN MENU           : 00 00 00 00 01
        PROGRAM PREFERENCES : 00 00 00 01 01
        DATA MANAGEMENT     : 00 00 00 02 01
        SIMULATION PAGE     : 00 00 00 03 01
        MANUAL ANALYSIS     : 00 00 00 04 01
        TRADE CONTROL       : 00 00 00 05 01
"""
#mousePos : [eventFlag(0), currentX(1), currentY(2), clickedFlag(3), releasedFlag(4), lastClickedX(5), lastClickedY(6), lastClickedButton(7), lastReleasedX(8), lastReleasedY(9), lastReleasedButton(10)]
mouseStat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

guiImages = []

class uiM_ButtonA:
    def __init__(self, x, y, w, h, imgIndex, txt):
        self.xPos = x
        self.yPos = y
        self.width = w
        self.height = h
        self.imgIndex = imgIndex
        self.status = 0 #0 : Default, 1 : Hovered, 2: Clicked, 3:Activated
        self.txt = txt

    def activateBox(self):
        self.active = True
    def deactivateBox(self):
        self.active = False

    def checkStatus(self):
        if self.status == 0:
            if ((self.xPos <= mouseStat[1]) and ((self.xPos + self.width) >= mouseStat[1])) and ((self.yPos <= mouseStat[2]) and ((self.yPos + self.height) >= mouseStat[2])):
                self.status = 1
        elif self.status == 1:
            if ((self.xPos > mouseStat[1]) or ((self.xPos + self.width) < mouseStat[1])) or ((self.yPos > mouseStat[2]) or ((self.yPos + self.height) < mouseStat[2])):
                self.status = 0
            elif mouseStat[3] == True:
                self.status = 2
        elif self.status == 2:
            if ((self.xPos > mouseStat[1]) or ((self.xPos + self.width) < mouseStat[1])) or ((self.yPos > mouseStat[2]) or ((self.yPos + self.height) < mouseStat[2])):
                self.status = 0
            elif mouseStat[4] == True:
                self.status = 0
                return True
        return False
    
    def draw(self, canvas):
        if self.status == 0:
            drawRectangle(canvas, self.xPos, self.yPos, self.width, self.height, "black")
            drawRectangle(canvas, self.xPos+1, self.yPos+1, self.width-2*1, self.height-2*1, "silver")
            canvas.create_text(self.xPos + self.width / 2, self.yPos + self.height / 2, text = self.txt, fill = "black")
        elif self.status == 1:
            drawRectangle(canvas, self.xPos-4, self.yPos-4, self.width+8, self.height+8, "black")
            drawRectangle(canvas, self.xPos-2, self.yPos-2, self.width+4, self.height+4, "white")
            drawRectangle(canvas, self.xPos, self.yPos, self.width, self.height, "black")
            drawRectangle(canvas, self.xPos+1, self.yPos+1, self.width-2*1, self.height-2*1, "silver")
            canvas.create_text(self.xPos + self.width / 2, self.yPos + self.height / 2, text = self.txt, fill = "black")
        elif self.status == 2:
            drawRectangle(canvas, self.xPos-4, self.yPos-4, self.width+8, self.height+8, "black")
            drawRectangle(canvas, self.xPos+2, self.yPos+2, self.width-4, self.height-4, "silver")
            canvas.create_text(self.xPos + self.width / 2, self.yPos + self.height / 2, text = self.txt, fill = "black")

    def drawHB(self, canvas):
        if self.status == 0:
            canvas.create_image(self.xPos, self.yPos, image = guiImages[0], anchor = "nw")
        elif self.status == 1:
            canvas.create_image(self.xPos, self.yPos, image = guiImages[1], anchor = "nw")
        elif self.status == 2:
            canvas.create_image(self.xPos, self.yPos, image = guiImages[2], anchor = "nw")

class uiM_CheckBox:
    def __init__(self):
        return 0

class uiM_Slider:
    def __init__(self):
        return 0

class uiM_TextBoxRO:
    def __init__(self):
        return 0

class uiM_TextBoxWrite:
    def __init__(self):
        return 0

class uiM_gaugeBar:
    def __init__(self, x, y, w, h, color, perc, showTxt):
        self.xPos = x
        self.yPos = y
        self.width = w
        self.height = h
        self.color = color
        self.percentage = perc
        self.showText = showTxt

        self.line = 1

    def setPerc(self, num):
        self.percentage = num
        if self.percentage > 100:
            self.percentage = 100
        elif self.percentage < 0:
            self.percentage = 0

    def draw(self, canvas):
        drawRectangle(canvas, self.xPos, self.yPos, self.width, self.height, "black")
        drawRectangle(canvas, self.xPos+self.line, self.yPos+self.line, self.width-2*self.line, self.height-2*self.line, "white")
        drawRectangle(canvas, self.xPos+self.line, self.yPos+self.line, int((self.width-2*self.line)*self.percentage/100), self.height-2*self.line, self.color)
        if (self.showText):
            canvas.create_text(self.xPos + self.width / 2, self.yPos + self.height / 2, text = int(self.percentage), fill = "black")

#Page Class -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class uiM_page:
    def __init__(self, address, mode):
        self.pageAdd = 0
        self.buttonsA = []
        self.gaugeBars = []
        self.devMode = True
        self.pageAdd = address
        self.deMode = mode

    def processData(self, manager):
        for i in range(0, len(self.buttonsA)):
            if self.buttonsA[i].checkStatus():
                doHBAction(manager, self.pageAdd, i)

        if self.pageAdd == 0:
            if self.gaugeBars[0].percentage == 100:
                manager.navAdd = 1
            else:
                self.gaugeBars[0].setPerc(self.gaugeBars[0].percentage+1)
        elif self.pageAdd == 1:
            return 0
        elif self.pageAdd == 101:
            return 0
        elif self.pageAdd == 201:
            return 0
        elif self.pageAdd == 301:
            return 0
        elif self.pageAdd == 401:
            return 0
        elif self.pageAdd == 501:
            return 0

    def drawPage(self, manager, canvas):
        for i in range(0,len(self.gaugeBars)):
            self.gaugeBars[i].draw(canvas)
        for i in range(0,len(self.buttonsA)):
            self.buttonsA[i].draw(canvas)

        if manager.devMode == True:
            canvas.create_text(1280,20, text = "[Mouse]X" + str(mouseStat[1]) + "Y" + str(mouseStat[2]) 
                               + "  [LC]X" + str(mouseStat[5]) + "Y" + str(mouseStat[6]) + "'" + str(mouseStat[7]) + "'" 
                               + "  [LR]X" + str(mouseStat[8]) + "Y" + str(mouseStat[9]) + "'" + str(mouseStat[10]) + "'", fill = "green")
            canvas.create_text(1280,40, text = "[Page Address]:" + str(self.pageAdd) + "  [Number of buttonAs]:" + str(len(self.buttonsA)), fill = "green")

            #Draw Hit Boxes Last for their transparency
            for i in range(0,len(self.buttonsA)):
                self.buttonsA[i].drawHB(canvas)

        if self.pageAdd == 0:
            return 0
        elif self.pageAdd == 1:
            canvas.create_line(120, 5, 120, 1435, fill = "black", width = 2)
            return 0
        elif self.pageAdd == 101:
            canvas.create_line(120, 5, 120, 1435, fill = "black", width = 2)
            return 0
        elif self.pageAdd == 201:
            canvas.create_line(120, 5, 120, 1435, fill = "black", width = 2)
            return 0
        elif self.pageAdd == 301:
            canvas.create_line(120, 5, 120, 1435, fill = "black", width = 2)
            return 0
        elif self.pageAdd == 401:
            canvas.create_line(120, 5, 120, 1435, fill = "black", width = 2)
            return 0
        elif self.pageAdd == 501:
            canvas.create_line(120, 5, 120, 1435, fill = "black", width = 2)
            return 0

    def enableDevMode(self):
        self.devMode = True
    def disableDevMode(self):
        self.devMode = False

    def addButton(self, x, y, w, h, imgIndex, txt):
        self.buttonsA.append(uiM_ButtonA(x, y, w, h, imgIndex, txt))

    def addGaugeBar(self, x, y, w, h, color, perc, showTxt):
        self.gaugeBars.append(uiM_gaugeBar(x, y, w, h, color, perc, showTxt))
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Main Class - Manager ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class uiManager:
    #Class Initialization -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, window, canvas, text):
        self.navAdd = 0
        self.devMode = True
        self.uiPages = []

        self.uiPages.append(uiM_page(0, self.devMode)) #INITIALIZATION PAGE
        self.uiPages.append(uiM_page(1, self.devMode)) #MAIN MENU
        self.uiPages.append(uiM_page(101, self.devMode)) #PROGRAM PREFERENCES
        self.uiPages.append(uiM_page(201, self.devMode)) #DATA MANAGEMENT
        self.uiPages.append(uiM_page(301, self.devMode)) #SIMULATION PAGE
        self.uiPages.append(uiM_page(401, self.devMode)) #MANUAL ANALYSIS
        self.uiPages.append(uiM_page(501, self.devMode)) #TRADE CONTROL
        
        loadGUIImages()

        setupPages(self.uiPages)

        bindKeys(window)
        
        text.configure(font=("Times New Roman", 12, 'bold'))
        
        print("UserInterface Manager Created!")
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Class Functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def updateUIData(self):
        for i in range(0,len(self.uiPages)):
            if self.navAdd == self.uiPages[i].pageAdd:
                self.uiPages[i].processData(self)
                break

        #Release Mouse Event Flags
        mouseStat[0] = 0
        mouseStat[3] = 0
        mouseStat[4] = 0

    def updateGraphics(self, window, canvas):
        canvas.delete("all")

        for i in range(0,len(self.uiPages)):
            if self.navAdd == self.uiPages[i].pageAdd:
                self.uiPages[i].drawPage(self, canvas)
                break

        canvas.pack()
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Auxillary Functions ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bindKeys(tkinter):
    tkinter.bind("<Key>", keyEvent)

    tkinter.bind("<Button>", clickMouse)
    tkinter.bind("<ButtonRelease>", releaseMouse)
    tkinter.bind("<Motion>", mouseMoved)

def canvasTest(canvas):
    numArray = [1, 5, 7, 5, 3, 7, 8, 4, 3, 6, 7, 3, 32, 65, 76, 4]
    for i in range(0, len(numArray)):
        drawRectangle(canvas, 100+i*5, 1000, 5, -numArray[i]*10, "blue")
    canvas.create_text(170, 500, text = "Hello", fill = "black", font = ("Helvetica 15 bold"))

def drawRectangle(canvas, xPos, yPos, width, height, color):
    canvas.create_rectangle(xPos, yPos, xPos+width, yPos+height, fill = color)

def setupPages(pages):
    add = 0
    for i in range(0, len(pages)):
        add = pages[i].pageAdd
        #PAGE 0 HITBOX SETUP
        if add == 0:
            pages[i].addGaugeBar(5, 1390, 2550, 45, "lightgrey", 10, True)
        #PAGE 1 HITBOX SETUP
        elif add == 1:
            pages[i].addButton(10, 10, 100, 100, "green", "PREFERENCES")
            pages[i].addButton(10, 120, 100, 100, "green", "DATA")
            pages[i].addButton(10, 230, 100, 100, "green", "SIMULATION")
            pages[i].addButton(10, 340, 100, 100, "green", "ANALYSIS")
            pages[i].addButton(10, 450, 100, 100, "green", "TRADE")
        #PAGE 101 HITBOX SETUP
        elif add == 101:
            pages[i].addButton(10, 10, 100, 100, "green", "MAIN MENU")
            pages[i].addButton(1280, 10, 100, 100, "blue", "SHOW HITBOX")
        #PAGE 201 HITBOX SETUP
        elif add == 201:
            pages[i].addButton(10, 10, 100, 100, "green", "MAIN MENU")
        #PAGE 301 HITBOX SETUP
        elif add == 301:
            pages[i].addButton(10, 10, 100, 100, "green", "MAIN MENU")
        #PAGE 401 HITBOX SETUP
        elif add == 401:
            pages[i].addButton(10, 10, 100, 100, "green", "MAIN MENU")
        #PAGE 501 HITBOX SETUP
        elif add == 501:
            pages[i].addButton(10, 10, 100, 100, "green", "MAIN MENU")

def getProjAddress():
    return os.path.dirname(os.path.realpath(__file__))

def loadGUIImages():
    #Load HitBox Image
    guiImages.append(ImageTk.PhotoImage(Image.new(mode = "RGBA", size = (100, 100), color = (255, 130, 130, 80))))
    guiImages.append(ImageTk.PhotoImage(Image.new(mode = "RGBA", size = (100, 100), color = (0, 255, 120, 80))))
    guiImages.append(ImageTk.PhotoImage(Image.new(mode = "RGBA", size = (100, 100), color = (0, 100, 255, 80))))

    #Load Test Image 1
    guiImages.append(ImageTk.PhotoImage(file = os.path.join(getProjAddress() + r"\rsc\imgs\tester1.png")))

def doHBAction(manager, pageAdd, hbIndex):
    #PAGE ADD 0 ----- INITIALIZATION PAGE
    if pageAdd == 0:
        #PAGE ADD 0 - HITBOX0
        if hbIndex == 0:
            manager.navAdd = 1
            print("Page 0 Box 0 Clicked!")
        #PAGE ADD 0 - HITBOX1
        elif hbIndex == 1:
            print("Page 0 Box 1 Clicked!")
    
    #PAGE ADD 1 ----- MAIN MENU
    elif pageAdd == 1:
        #PAGE ADD 1 - HITBOX0
        if hbIndex == 0:
            manager.navAdd = 101
            print("Page 1 Box 0 Clicked!")
        #PAGE ADD 1 - HITBOX1
        elif hbIndex == 1:
            manager.navAdd = 201
            print("Page 1 Box 1 Clicked!")
        #PAGE ADD 1 - HITBOX1
        elif hbIndex == 2:
            manager.navAdd = 301
            print("Page 1 Box 2 Clicked!")
        #PAGE ADD 1 - HITBOX1
        elif hbIndex == 3:
            manager.navAdd = 401
            print("Page 1 Box 3 Clicked!")
        #PAGE ADD 1 - HITBOX1
        elif hbIndex == 4:
            manager.navAdd = 501
            print("Page 1 Box 4 Clicked!")
    
    #PAGE ADD 101 ----- PREFERENCES
    elif pageAdd == 101:
        if hbIndex == 0:
            manager.navAdd = 1
            print("Page 101 Box 0 Clicked!")
        elif hbIndex == 1:
            manager.devMode = ~manager.devMode
            print("Page 101 Box 1 Clicked!")
    
    #PAGE ADD 201 ----- DATA
    elif pageAdd == 201:
        if hbIndex == 0:
            manager.navAdd = 1
            print("Page 201 Box 0 Clicked!")
        elif hbIndex == 1:
            print("Page 201 Box 1 Clicked!")
    
    #PAGE ADD 301 ----- SIMULATION
    elif pageAdd == 301:
        if hbIndex == 0:
            manager.navAdd = 1
            print("Page 301 Box 0 Clicked!")
        elif hbIndex == 1:
            print("Page 301 Box 1 Clicked!")
    
    #PAGE ADD 401 ----- ANALYSIS
    elif pageAdd == 401:
        if hbIndex == 0:
            manager.navAdd = 1
            print("Page 401 Box 0 Clicked!")
        elif hbIndex == 1:
            print("Page 401 Box 1 Clicked!")
    
    #PAGE ADD 501 ----- TRADE
    elif pageAdd == 501:
        if hbIndex == 0:
            manager.navAdd = 1
            print("Page 501 Box 0 Clicked!")
        elif hbIndex == 1:
            print("Page 501 Box 1 Clicked!")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Input Event Functions --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def keyEvent(event):
    print (event.keycode)

def clickMouse(event):
    mouseStat[5] = mouseStat[1]
    mouseStat[6] = mouseStat[2]
    mouseStat[7] = event.num
    mouseStat[3] = 1
    mouseStat[0] = 1

def releaseMouse(event):
    mouseStat[8] = mouseStat[1]
    mouseStat[9] = mouseStat[2]
    mouseStat[10] = event.num
    mouseStat[4] = 1
    mouseStat[0] = 1

def mouseMoved(event):
    mouseStat[1] = event.x
    mouseStat[2] = event.y
    mouseStat[0] = 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


