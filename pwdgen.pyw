#password generator by Coup23
#github.com/Coup23
#github.com/CSK-Company
from tkinter import *
import secrets
import string

root = Tk()
root.title('pwdgen')
root.geometry('350x200')
root.resizable(False, False)
root.iconbitmap(default='Logo.ico') 

# label
l = Label(root, text="password length:")
l.pack()
l.place(x=0, y=0)

# entry box pwd legth
lbox = Entry(root, width=15)
lbox.insert(END, '20')
lbox.pack()
lbox.place(x=0, y=25)

# pwdbox
pwd_area = Text(root, height=10, width=30)
pwd_area.pack()
pwd_area.place(x=100, y=0)


def clickExitButton():
    input = int(lbox.get())
    if input < 16:
        size = 16
    else:
        size = int(lbox.get())

    chars = string.digits + string.ascii_letters + string.punctuation
    while True:
        pwd = ''.join(secrets.choice(chars) for _ in range(size))
        if (any(c.islower() for c in pwd)
                and any(c.isupper() for c in pwd)
                and sum(c.isdigit() for c in pwd) >= 3):
            break
    pwd_area.delete("1.0", "end")
    pwd_area.insert(END, pwd)


# create button, link it to clickExitButton()
exitButton = Button(root, text="genarate", command=clickExitButton)
# place button at (0,0)
exitButton.place(x=20, y=50)

root.mainloop()
