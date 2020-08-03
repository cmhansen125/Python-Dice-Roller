import tkinter
from tkinter import *
from Guts import guts


def main():
    window = tkinter.Tk()
    mainFrame = tkinter.Frame(
        width=5,
        height=5,
    )
    mainFrame.pack()
    greeting = tkinter.Label(mainFrame, text="Dice Roller!")
    greeting.pack(side=TOP)

    var = tkinter.StringVar()
    button20 = tkinter.Button(
        mainFrame,
        text="D20",
        width=5,
        height=1,
        command=lambda: diceRoller(20)
    )
    button100 = tkinter.Button(
        mainFrame,
        text="D100",
        width=5,
        height=1,
        command=lambda: diceRoller(100)
    )
    button10 = tkinter.Button(
        mainFrame,
        text="D10",
        width=5,
        height=1,
        command=lambda: diceRoller(10)
    )
    button8 = tkinter.Button(
        mainFrame,
        text="D8",
        width=5,
        height=1,
        command=lambda: diceRoller(8)
    )
    button6 = tkinter.Button(
        mainFrame,
        text="D6",
        width=5,
        height=1,
        command=lambda: diceRoller(6)
    )
    button4 = tkinter.Button(
        mainFrame,
        text="D4",
        width=5,
        height=1,
        command=lambda: diceRoller(4)
    )

    def diceRoller(size):
        print("clicked on", size)
        result = str(guts(size))
        print(result)
        message = ""
        if result == "1":
            print(1)
            message += "Bad Luck! \n"
        message += "You rolled a: \n"
        message += result
        var.set(message)

    button20.pack()
    button100.pack()
    button10.pack()
    button8.pack()
    button6.pack()
    button4.pack()

    bottomFrame = tkinter.Frame()
    bottomFrame.pack()

    label = tkinter.Message(bottomFrame, textvariable=var)
    var.set("Pick a die to roll!")
    label.pack(side=BOTTOM)

    window.mainloop()


main()
