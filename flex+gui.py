from tkinter import *
from tkinter import messagebox
import csv

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

reader = 0
your_list = 0

listFlex = []

def countFlex():       

    global inFlex
    global utFlex
    global totFlex
    global reader
    global listFlex

    inFlex = int(inFlex) + int(inInput.get() or 0)
    utFlex = int(utFlex) + int(utInput.get() or 0)
    
        
    print('\nIN', inFlex)
    print('UT', utFlex)

    totFlex = int(inFlex) - int(utFlex)
    print('TOT',totFlex, '\n')

'''    
    try:
        with open('test.csv', 'r') as f:
            reader = csv.reader(f)
            listFlex = list(reader)
    except:
        print('1 öppningen')
            
    listFlex.insert(0, totFlex)


    with open('test.csv', 'a', newline='') as csvFlexImport:
        csvFlex = csv.writer(csvFlexImport, delimiter=',')
        csvFlex.writerow(listFlex)

    print('listFlex:', listFlex)
    
'''
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
