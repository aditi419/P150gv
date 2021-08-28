from tkinter import * 
import random 

root = Tk()
root.title('Random Countries and Capitals')
root.geometry('500x500')

countryInput = Entry(root)
capitalInput = Entry(root)

countryListLabel = Label(root)
capitalListLabel = Label(root)
randomCountryNum = Label(root)
randomCapitalNum = Label(root)

countryList = []
capitalList = []

def stuff():
    countryInputName = countryInput.get()
    countryList.append(countryInputName)
    countryListLabel['text'] = 'Country Name : ' + str(countryList)
    
    capitalInputName = capitalInput.get()
    capitalList.append(capitalInputName)
    capitalListLabel['text'] = 'City Name : ' + str(capitalList)
    

def what():
     randomNum = random.randint(0,len(countryListLabel))
     randomNum2 = random.randint(0,len(capitalListLabel))
     randomCountryNum['text'] = 'Random Country : ' + str(randomNum)
     randomCapitalNum['text'] = 'Random City : ' + str(randomNum2)


btn =  Button(root,text = 'Display Country and City Name',command = stuff)
btn2 =  Button(root,text = 'Display Country and City Name Randomly',command = what)


countryInput.place(relx = 0.5,rely = 0.1,anchor = CENTER)
capitalInput.place(relx = 0.5,rely = 0.2,anchor = CENTER)
btn.place(relx = 0.5,rely = 0.3,anchor = CENTER)
countryListLabel.place(relx = 0.5,rely = 0.4,anchor = CENTER)
capitalListLabel.place(relx = 0.5,rely = 0.5,anchor = CENTER)
btn2.place(relx = 0.5,rely = 0.6,anchor = CENTER)
randomCountryNum.place(relx = 0.5,rely = 0.7,anchor = CENTER)
randomCountryNum.place(relx = 0.5,rely = 0.8,anchor = CENTER)



mainloop()
