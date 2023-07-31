import tkinter as tk

def convert_temperature():
    try:
        temperature = float(input_entry.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            converted_temperature = (temperature * 9/5) + 32
            result_label.config(text=f"{temperature}°C is {converted_temperature:.2f}°F")
        elif var.get() == 2:  # Fahrenheit to Celsius
            converted_temperature = (temperature - 32) * 5/9
            result_label.config(text=f"{temperature}°F is {converted_temperature:.2f}°C")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature.")

root = tk.Tk()
root.title("Temperature Converter")

var = tk.IntVar()

input_label = tk.Label(root, text="Enter Temperature:")
input_label.pack(pady=10)

input_entry = tk.Entry(root)
input_entry.pack()

radio_frame = tk.Frame(root)
radio_frame.pack(pady=5)

celsius_radio = tk.Radiobutton(radio_frame, text="Celsius to Fahrenheit", variable=var, value=1)
celsius_radio.pack(side=tk.LEFT, padx=5)

fahrenheit_radio = tk.Radiobutton(radio_frame, text="Fahrenheit to Celsius", variable=var, value=2)
fahrenheit_radio.pack(side=tk.LEFT, padx=5)

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

root.mainloop()