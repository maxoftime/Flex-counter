    # Load modules and defining variables #
from tkinter import *
from tkinter import messagebox

master = Tk()

outFlex = 0
inFlex = 0
totFlexLabel = StringVar()

    # Display the entry fields #
inInput = Entry(master, width=50)
inInput.pack()
inInput.focus_set()
outInput = Entry(master, width=50)
outInput.pack()

    # Read the data from Flextid.txt #
with open('Flextid.txt', 'r') as totFlexOpen:
    totFlexRead = totFlexOpen.read()

    # Function for the calculations #
def countFlex():       

        # Load global variables #
    global inFlex
    global outFlex
    global totFlexRead
    
        # Assign the input to in and out variables #
    inFlex = int(inFlex) + int(inInput.get() or 0)
    outFlex = int(outFlex) + int(outInput.get() or 0)

        # Sum up the new total flex #
    totFlexNew = int(inFlex) - int(outFlex)    
    totFlex = int(totFlexRead) + totFlexNew

        # Write the current totFlex to Flextid.txt #
    with open('Flextid.txt', 'w') as totFlexOpen:
        totFlexOpen.write(str(totFlex))

        # Set label to the correct value #
    if totFlex > 0:
        totFlexLabel.set('Du har %d intjänade minuter' % totFlex)

    elif totFlex < 0:
        totFlex = int(totFlex) * -1
        totFlexLabel.set('Du har %d minouter att ta igen' % totFlex)

    else:
        totFlexLabel.set('Du har inget sparat och inget att ta av tyvärr.')
        

    # Set label to a starting value, when read from Flextid.txt #
if int(totFlexRead) > 0:
        totFlexLabel.set('Du har %s intjänade minuter' % str(totFlexRead))

elif int(totFlexRead) < 0:
        totFlexRead = int(totFlexRead) * -1
        totFlexLabel.set('Du har %s minuter att ta igen' % str(totFlexRead))

else:
        totFlexLabel.set('Du har inget sparat och inget att ta av tyvärr.')

    # Display the button and the label #
skickaKnapp = Button(master, text="Räkna", width=42, command=countFlex).pack()
Label(master, textvariable=totFlexLabel).pack()

mainloop()
