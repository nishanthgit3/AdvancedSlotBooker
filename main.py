from tkinter import *

# Root window
root  = Tk()
root.title("Advanced Slot Booker")
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)
root.geometry("925x800")

# Functions
def cookieButtonClick():
    cookie = cookieEntry.get()

# Creating
# Row 1
cookieText = Label(root, text="Cookie")
cookieEntry = Entry(root, width=50)
cookieButton = Button(root, text="✓", command=cookieButtonClick)

# Showing
cookieText.grid(row=0, column=0)
cookieEntry.grid(row=0, column=1)
cookieButton.grid(row=0, column=2)


root.mainloop()