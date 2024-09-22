import customtkinter as ctk

#unit conversions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature():
    try: #error handler
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result_var.set(f"{temp:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K") #fetch results to display them on GUI
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result_var.set(f"{temp:.2f}°F = {celsius:.2f}°C = {kelvin:.2f}K")
        elif unit == 'K':
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result_var.set(f"{temp:.2f}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
        else:
            result_var.set("Invalid unit. Use C, F, or K.") #unit error handler
    except ValueError:
        result_var.set("Please enter a valid number.") #number error handler

#setting up the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Temperature Converter")
app.geometry("400x300")

#temperature input
label_temp = ctk.CTkLabel(app, text="Enter temperature:")
label_temp.pack(pady=10)

entry_temp = ctk.CTkEntry(app)
entry_temp.pack(pady=10)

#unit selection
label_unit = ctk.CTkLabel(app, text="Select unit (Celsius/Fahrenheit/Kelvin):")
label_unit.pack(pady=10)

combo_unit = ctk.CTkComboBox(app, values=["C", "F", "K"])
combo_unit.pack(pady=10)

#convert button
button_convert = ctk.CTkButton(app, text="Convert", command=convert_temperature)
button_convert.pack(pady=20)

#result display
result_var = ctk.StringVar()
label_result = ctk.CTkLabel(app, textvariable=result_var, wraplength=300)
label_result.pack(pady=10)

#start application
app.mainloop()