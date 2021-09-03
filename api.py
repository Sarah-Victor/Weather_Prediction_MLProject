import tkinter as tk
import time

	def getWeather(canvas):
	    city = textField.get()
	   
	

	    json_data = requests.get(api).json()
	    condition = json_data['weather'][0]['main']
	    temp = int(json_data['main']['temp'] - 273.15)
	    min_temp = int(json_data['main']['temp_min'] - 273.15)
	    max_temp = int(json_data['main']['temp_max'] - 273.15)
	    pressure = json_data['main']['pressure']
	    humidity = json_data['main']['humidity']
	    wind = json_data['wind']['speed']
	    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
	    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
	

	    final_info = condition + "\n" + str(temp) + "°C" 
	    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
	    label1.config(text = final_info,foreground = "white",bg="#8C001A")
	    label2.config(text = final_data,foreground = "white",bg="#8C001A")
	canvas = tk.Tk()
	canvas.geometry("600x500")
	canvas.configure(bg='#8C001A')
	canvas.title("Weather App")
	f = ("poppins", 15, "bold")
	t = ("poppins", 35, "bold")
	label3 = tk.Label(canvas,borderwidth = 4,font=f)
	label3.pack()
	switch = "\n" + "Enter your city:" + "\n"
	label3.config(text = switch,foreground = "white",bg="#8C001A") 
	textField = tk.Entry(canvas,justify='center', width = 20, font = t,foreground="white")
	textField.configure(bg="#C04000", insertbackground='black')
	textField.pack(pady = 20)
	textField.focus()
	textField.bind('<Return>', getWeather)
	

	label1 = tk.Label(canvas, font=t)
	label1.pack()
	label2 = tk.Label(canvas, font=f)
	label2.pack()
	canvas.mainloop() 
