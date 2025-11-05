from PIL import Image
import tkinter as tk
from tkinter import messagebox

# --- Step 1: Load the image ---
input_filename = "220401002.jpg"
output_filename = "220401002_converted.jpeg"

# Open image
image = Image.open(input_filename)

# --- Step 2: Show an alert message ---
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window
messagebox.showinfo("Conversion Notice", "Daniel Kanybekov 25118080902")

# --- Step 3: Save image as JPEG ---
image.save(output_filename, "JPEG")

print(f"Image successfully converted and saved as {output_filename}")
