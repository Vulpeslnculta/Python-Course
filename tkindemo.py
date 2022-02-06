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
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0
            # fill=tkinter.BOTH, expand=True
            )
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="Testing1")
button2 = tkinter.Button(rightFrame, text="Testing2")
button3 = tkinter.Button(rightFrame, text="Testing3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='ns')
rightFrame.columnconfigure(0, weight=1)

mainWindow.mainloop()

