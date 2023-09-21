# Import the tkinter library for creating a GUI.
import tkinter as tk

# Import the choice function from the random library.
from random import *

# Define character sets for the password.
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letters
digit = "0123456789"  # Numbers
special = "!@#$%^&*()-+=;:'\/`~,<>?"  # Special characters

# Function to generate a random password.
def generate_password():
    # Generate an 10-character password by randomly selecting characters from the defined character sets.
    password = ''.join([choice(alphabet + digit + special) for _ in range(10)])  # Generating a 10-character password
    # Update the text of the password_label with the generated password.
    password_label.config(text=password)

# Create the main application window.
app = tk.Tk()
app.title("Random Password Generator")

# Create a label widget for the greeting.
greeting_label = tk.Label(app, text="Greetings! Step into the PassWord Generator.", font=("Arial", 16))
greeting_label.pack(padx=20, pady=20)

# Create a label widget to display the generated password.
password_label = tk.Label(app, text="", font=("Arial", 16))
password_label.pack(padx=20, pady=10)

# Create a button widget to trigger password generation.
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(padx=20, pady=10)

# Start the GUI event loop to handle user interactions.
app.mainloop()
