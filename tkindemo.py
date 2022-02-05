try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# tkinter._test()
#
mainWindow = tkinter.Tk()

mainWindow.title("Testing")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="TESTING CANVAS")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side="top", anchor='n'
            # fill=tkinter.BOTH, expand=True
            )
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(mainWindow, text="Testing1")
button2 = tkinter.Button(mainWindow, text="Testing2")
button3 = tkinter.Button(mainWindow, text="Testing3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()

