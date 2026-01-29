import json
import requests
from tkinter import *

# Root window
root  = Tk()
root.title("Advanced Slot Booker")
icon = PhotoImage(file="logo.png")
root.iconphoto(True, icon)
root.geometry("925x800")

# Functions

# Logics
def getCourse():
    url = 'https://ps.bitsathy.ac.in/api/ps_v2/my-course?tab=personalizedSkills'
    try:
        r = requests.get(url, headers=headers)
        data = r.json()
    except:
        print("Please enter a cookie before requesting for the courses")

# GUI
def cookieButtonClick():
    cookie = cookieEntry.get()
    headers = {'Host':'ps.bitsathy.ac.in', 'Cookie': 'PS='+cookie}

# Creating
# Row 1
cookieText = Label(root, text="Cookie")
cookieEntry = Entry(root, width=50)
cookieButton = Button(root, text="✓", command=cookieButtonClick)

# Row 2
# coursesMenu = OptionMenu(root, course, "")

# Showing/Grids
cookieText.grid(row=0, column=0)
cookieEntry.grid(row=0, column=1)
cookieButton.grid(row=0, column=2)

















root.mainloop()