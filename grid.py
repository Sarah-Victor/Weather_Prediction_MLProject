from tkinter import *

def weather():
    import Api
    Api.mains()
def tomorrow():
    import rainfall
    rainfall.possible_rain()
def analyze():
    import rainfall
    rainfall.analyze()
root = Tk() #makes a blank popup, under the variable name 'root'
topFrame = Frame(root,bg="#837E7C")
root.geometry("1000x900")
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
root.title("Weather App")
root.configure(bg='#2C3539')
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
label1 = Label(topFrame,borderwidth = 1,font = t)
label1.pack()
title = "\n" + "WEATHER REPORT " + "\n" 
label1.config(text = title,foreground = "white",bg="#837E7C",width = 20)
button3 = Button(topFrame, text='Analyze avarage rainfall every month for india', fg='green',command = analyze,font = f,bg='#0C090A')
button1 = Button(topFrame, text='Current weather report for specific city..........',command = weather, fg='red',font = f,bg='#0C090A')
button2 = Button(topFrame, text='Do you need to predict rainfall tomorrow......?', fg='blue',command = tomorrow,font = f,bg='#0C090A')
#button4 = Button(topFrame, text='Button 4', fg='pink')
button2.pack(side=BOTTOM,padx=20, pady=20)
button3.pack(side=BOTTOM,padx=20, pady=20)
button1.pack(side=BOTTOM,padx=20, pady=20)
#button4.pack(side=BOTTOM)

root.mainloop() #loops the program forever until its closed
