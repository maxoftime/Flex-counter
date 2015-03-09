from tkinter import *
from tkinter import messagebox
'''
root = Tk()
root.title('gridtest')
root.geometry('400x800')

frame1 = Frame(root, bg='red')
frame1.grid(ipadx='10', ipady='10')
label1 = Label(frame1, text='Ruta 1', bg='#666666')
label1.grid()

root.mainloop()
'''
'''
class GUI:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame,
                             text='sluta upp',
                             command=frame.quit,
                             width=40,
                             height=10,
                             bg='#f00',
                             font='Futura',
                             relief=FLAT)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text='hejsan', command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print('hi there you')
        

root = Tk()
gui = GUI(root)

root.mainloop()
root.destroy()

'''

master = Tk()

inInputEntry = Entry(master, width=50)
inInputEntry.pack()
inInputEntry.focus_set()

utInputEntry = Entry(master, width=50)
utInputEntry.pack()

utFlex = 0
totFlex = 0
inFlex = 0
totFlex = IntVar()


def countFlex():       

    global inFlex
    global utFlex
    global totFlex

    inInput = inInputEntry.get()
    utInput = utInputEntry.get()
    
    try:
        inFlex = int(inFlex) + int(inInput or 0)
        utFlex = int(utFlex) + int(utInput or 0)
             
    except ValueError as ingenSiffraIn:
        inFlex = int(inFlex)
        utFlex = int(utFlex)
        messagebox.showerror("Du måste skriva en siffra", "Skriv en siffra istället")

    except Exception as annatFel:
        inFlex = int(inFlex)
        utFlex = int(utFlex)
        messagebox.showerror("Nu blev det något knas")
        
        
    print('IN', inFlex)
    print('UT', utFlex)


    totFlex = int(inFlex) - int(utFlex)
    '''
    if totFlex < 0:
            totFlexPos = totFlex * -1
            
            totFlexMessage.set('Du har',totFlexPos,'flexminuter att ta igen.')

    elif totFlex == 0:
            totFlexMessage.set('\nDu har inga intjänade flexminuter.\n')

    else:
            totFlexMessage.set('\nDu har',totFlex, 'intjänade flexminuter.\n')
    '''
    print('TOT',totFlex, '\n')
     
skickaKnapp = Button(master, text="Räkna", width=42, command=countFlex)
skickaKnapp.pack()


Label(master, textvariable=totFlex).pack()

mainloop()

'''
e = Entry(master, width=50)
e.pack()





def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")

content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)

'''
