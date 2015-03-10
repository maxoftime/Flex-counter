from tkinter import *
from tkinter import messagebox

master = Tk()

inInput = Entry(master, width=50)
inInput.pack()
inInput.focus_set()

utInput = Entry(master, width=50)
utInput.pack()

utFlex = 0
totFlex = 0
inFlex = 0
totFlex = IntVar()



def countFlex():       

    global inFlex
    global utFlex
    global totFlex
    '''
    try:
        inFlex = int(inFlex) + int(inInput.get() or 0)
        utFlex = int(utFlex) + int(utInput.get() or 0)
             
    except ValueError as ingenSiffraIn:
        messagebox.showerror("Du måste skriva en siffra", "Skriv en siffra istället")

    '''

    inFlex = int(inFlex) + int(inInput.get() or 0)
    utFlex = int(utFlex) + int(utInput.get() or 0)
    
        
    print('IN', inFlex)
    print('UT', utFlex)


    totFlex = int(inFlex) - int(utFlex)
    print('TOT',totFlex, '\n')
     
skickaKnapp = Button(master, text="Räkna", width=42, command=countFlex)
skickaKnapp.pack()


Label(master, textvariable=totFlex).pack()

mainloop()
