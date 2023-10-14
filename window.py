from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    499.5, 131.5,
    text = "AUTOMATIC  QUESTION AND ANSWER GENERATOR",
    fill = "#ffffff",
    font = ("Inter-Light", int(50.0)))

canvas.create_text(
    499.5, 270.0,
    text = "Smart solutions made easy and accessible",
    fill = "#ffffff",
    font = ("Inter-Light", int(16.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 423, y = 377,
    width = 154,
    height = 45)

window.resizable(False, False)
window.mainloop()
