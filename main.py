from tkinter import *

root  = Tk()

# Functions
def cookieButtonClick():
    cookie = cookieEntry.get()
    print(cookie)

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