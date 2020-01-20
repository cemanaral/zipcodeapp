from tkinter import *
import zipcodeapp

root = Tk()
root.title('ZipCodeApp')
root.iconbitmap('icon.ico')

def process():
    in_zip = myEntry.get()
    zipcodeapp.main(in_zip)
    name = zipcodeapp.name
    population = zipcodeapp.population
    info_text = 'Name: {1}\nPopulation: {0}'.format(population, name)
    global myLabel1
    try:
        myLabel1.destroy()
    except:
        pass
    myLabel1 = Label(root, text=info_text)
    myLabel1.grid(row=1, column=0, columnspan=2)


# making and placing buttons
myButton = Button(root, text='Process', command=process)
myButton.grid(row=0, column=0)

myEntry = Entry(root)
myEntry.grid(row=0, column=1, padx=40)

myLabel2 = Label(root, text='zip code must be from the us\nCem Anaral, 2019')
myLabel2.grid(row=2, column=0, columnspan=2)


root.mainloop()
