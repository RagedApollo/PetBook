#import section
from tkinter import *
from tkinter import messagebox
buttonTXT = "Login"
TitelOfPage = "PetBook"
bt_signup = "signup"





 ### define shit ###
username = ""
password = ""
users = []
class user:
    def __init__(username, password):
        user.username = username
        user.password = password
        users.append(user)


def CreateUserInfo(self, username, password):
    user.username = input("How do you want to be your username?")
    if user.username.lengt <= 5:
        user.username = ""
        print("Is too short")
    
    user.password = input("What do you want your password to be?")
    if user.password.length <= 5:
        user.password = ""
        print("password too short")
def getUserInfo(self, username, password):
    currentUser = user.username
    currentPassword = user.password
def GetPet(self):
    self.pet = input("what kind of pet is it?")
def loadHome():
    pass

def getValueandDecide():
    filledUsername = txtfielduser.get()
    filledPassword = txtfieldpass.get()
    if filledUsername == user.username:
        loadHome()
    else:
        pass
def setValuesForX():
    currentuser = user(user.password)
    user().user = txtfielduser.get()
    print(user(username, password).username)

### do shit ###
window = Tk()
#widgets I go

#button1
btn = Button(window, text= buttonTXT, fg="blue", command=getValueandDecide)
btn.place(x=80, y=100)

BUTTON_LOGIN = Button(window, text=bt_signup, fg="blue", command = setValuesForX)
BUTTON_LOGIN.place(x=80, y=10)
#button1END

#label1
lbltitle = Label(window, text= TitelOfPage, fg="red", font=("comic sans", 32))
lbltitle.place(x=250,y=50)


lbluser = Label(window, text= "Username", fg="black", font=("comic sans", 11))
lbluser.place(x=80, y=130)

lblpass = Label(window, text= "Password", fg="black", font=("comic sans", 11))
lblpass.place(x=80, y=230)
#label1END

#create text field
txtfielduser = Entry(window, text="This is a textpromt", bg='white', fg="black", bd=10)
txtfielduser.place(x=80, y=150)

txtfieldpass = Entry(window, text="this is a textprompt", bg='white', fg='black', bd=10)
txtfieldpass.place(x=80, y=250)






#widgets I end
window.title('PetBook')
window.geometry("700x500+10+10")
window.mainloop()
