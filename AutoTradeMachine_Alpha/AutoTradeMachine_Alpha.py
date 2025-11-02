#Base Modules
import tkinter
import time
from PIL import Image, ImageTk

#ATM Modules
from ATM_recordManager import recordManager
from ATM_uiManager import uiManager
from ATM_accessManager import accessManager
from ATM_analysisManager import analysisManager

#Initialization Sequence ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Window and Canvas Initialization
print("INITIALIZING.....\n")

window = tkinter.Tk() #Window Class Creation
canvas = tkinter.Canvas(window, width = 2560, height = 1440, bg = "white", bd = 2)
text = tkinter.Text(window)

window.title("ATM_ALPHA") #Window Title
window.geometry("1920x1080+100+100") #Window size setting, 1920x1080
window.resizable(False,False) #Disable window resizing
window.attributes("-fullscreen", False) #Set the window to start as fullscreen mode
window.bind("<F11>", lambda event: window.attributes("-fullscreen", not window.attributes("-fullscreen"))) #Enables F11 Key to go to and escape from fullScreen Mode
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False)) #Enables ESC Key to escape from fullScreen Mode

#ATM Modules Initialization
uiMan = uiManager(window, canvas, text)
recordMan = recordManager()
accessMan = accessManager()
analysisMan = analysisManager()
print("\nINITIALIZATION COMPLETED!!!\n")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Mainer Functions -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mainerAlpha():
    functionT = 10

    print(time.time())
    uiMan.updateUIData()
    uiMan.updateGraphics(window, canvas)
    window.after(functionT, mainerAlpha)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#accessMan.getData()
#accessMan.getBalance()

window.after(0, mainerAlpha)
window.mainloop()



