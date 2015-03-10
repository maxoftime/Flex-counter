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
totFlexLabel = StringVar()


def countFlex():       

    global inFlex
    global utFlex
    global totFlex

    

    inFlex = int(inFlex) + int(inInput.get() or 0)
    utFlex = int(utFlex) + int(utInput.get() or 0)
    
        
    print('IN', inFlex)
    print('UT', utFlex)


    totFlex = int(inFlex) - int(utFlex)
    print('TOT',totFlex, '\n')

    saveFile = open('Flextid.txt','a')
    saveFile.write('%s\n' % str(totFlex))
    saveFile.close()

    if totFlex > 0:
        totFlexLabel.set('Du har %d intjänade minuter' % totFlex)

    elif totFlex < 0:
        totFlex = int(totFlex) * -1
        totFlexLabel.set('Du har %d minuter att ta igen' % totFlex)

    else:
        totFlexLabel.set('Du har inget sparat och inget att ta av tyvärr. \(*.*)/')

    

skickaKnapp = Button(master, text="Räkna", width=42, command=countFlex).pack()
Label(master, textvariable=totFlexLabel).pack()

mainloop()
