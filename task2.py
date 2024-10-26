import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        result_label.config(text=f"BMI: {bmi} - {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
root = tk.Tk()
root.title("BMI Calculator")
tk.Label(root, text="Enter Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)
tk.Label(root, text="Enter Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="Your BMI will appear here.")
result_label.pack(pady=10)
root.mainloop()
