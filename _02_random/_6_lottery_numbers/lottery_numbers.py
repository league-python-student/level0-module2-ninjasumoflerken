import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    a = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    b = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    c = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    d = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    e = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    f = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    messagebox.showinfo(messagebox.showinfo(title="Lottery", message = "Your Numbers Are "+ str(a)+" "+ str(b)+" "+ str(c)+" "+ str(d)+" "+ str(e)+ " "+ str(f)))
    num = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    numb = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    numbe = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    number = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    number1 = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    number2 = random.randint(0, 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    messagebox.showinfo(messagebox.showinfo(title="Lottery", message = "The Winning Numbers Are "+ str(num)+" "+ str(numb)+" "+ str(numbe)+" "+ str(number)+" "+ str(number1)+ " "+ str(number2)))
    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
