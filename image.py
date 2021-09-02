import tkinter as tk
def api_image():
    import api
    api.mains()
    
if __name__ == "__main__":
    canvas = tk.Tk()
    canvas.geometry("1200x1100")
    canvas.title("Weather App")
    #canvas.configure(bg='#6b8e23')
    f = ("poppins", 15, "bold",)
    t = ("poppins", 35, "bold")
    button = Button(canvas,
	text = 'apipross',
	command = api_image)  
    button.pack()  
  
    canvas.mainloop()
