import random
from tkinter import *

# add a collection of quotes and author pairs
quotes = [
    {"quote": "Life is too short and sweet to be spent by cribbing and complaining about things." +
    "Here are some random quotes about the most wonderful gift that we've got.",
    "author": "Life"
    },
    {"quote": "Humor is richly rewarding to the person who employs it." +
    "It has some value in gaining and holding attention." +
    "But it has no persuasive value at all.",
    "author": "John Kenneth Galbraith"
    },
    {"quote": "God save me from my friends. I can protect myself from my enemies.",
    "author": "Claude Louis Hector de Villars "
    },
    {"quote": "The price of anything is the amount of life you exchange for it.",
    "author": "David Thoreau"
    },
    {"quote": "Life is like a landscape. You live in the midst of it but can" +
    "describe it only from the vantage point of distance. ",
    "author": "Charles Lindbergh"
    },
    {
    "quote": "A critic is someone who never actually goes to the battle," +
    "yet who afterwards comes out shooting the wounded.",
    "author": "Tyne Daly"
    }]
      
leng = len(quotes)

# function to display a random quote
def displayQuote() :
    rand = random.randint(0, leng - 1)
    x = quotes[rand]["quote"]
    y = quotes[rand]["author"]
    print('\n' + x + '\nAuthor: ' + y + '\n')

# create the window for the button
gui = Tk(className = 'myButton')
gui.geometry('500x200') 

#create and style button
button = Button(gui, text='Change Quote', width=40, height=3, bg='#8eb4d7',fg='#000000',
activebackground='#2e5b84', activeforeground='#ffffff',font='arial' , command = displayQuote)
button.pack()
gui.mainloop()