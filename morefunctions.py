import math

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size
        plot(canvas, x, y)



def draw_Axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0,  x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())


def plot(page, x, y):
    canvas.create_line(x, -y, x + 1, -y + 1, fill='red')


def circle(page, radius, g, h, color='red'):
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius**2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background='violet')
# canvas2.grid(row=0, column=1)


draw_Axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100, 'violet')
circle(canvas, 100, -100, 100, 'cyan')
mainWindow.mainloop()