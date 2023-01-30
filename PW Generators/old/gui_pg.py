import random
import string
import tkinter as tk

class PasswordGenerator(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Password Generator")
    self.geometry("300x150")

    # Create the widgets
    length_label = tk.Label(self, text="Length:") ;fg="white"
    self.length_field = tk.Entry(self)
    uppercase_label = tk.Label(self, text="Include uppercase characters?")
    self.uppercase_var = tk.IntVar()
    uppercase_checkbox = tk.Checkbutton(self, variable=self.uppercase_var)
    lowercase_label = tk.Label(self, text="Include lowercase characters?")
    self.lowercase_var = tk.IntVar()
    lowercase_checkbox = tk.Checkbutton(self, variable=self.lowercase_var)
    numbers_label = tk.Label(self, text="Include numbers?")
    self.numbers_var = tk.IntVar()
    numbers_checkbox = tk.Checkbutton(self, variable=self.numbers_var)
    symbols_label = tk.Label(self, text="Include symbols?")
    self.symbols_var = tk.IntVar()
    symbols_checkbox = tk.Checkbutton(self, variable=self.symbols_var)
    generate_button = tk.Button(self, text="Generate", command=self.generatePassword)
    self.password_field = tk.Entry(self, state="readonly")

    # Add the widgets to the window
    length_label.grid(row=0, column=0)
    self.length_field.grid(row=0, column=1)
    uppercase_label.grid(row=1, column=0)
    uppercase_checkbox.grid(row=1, column=1)
    lowercase_label.grid(row=2, column=0)
    lowercase_checkbox.grid(row=2, column=1)
    numbers_label.grid(row=3, column=0)
    numbers_checkbox.grid(row=3, column=1)
    symbols_label.grid(row=4, column=0)
    symbols_checkbox.grid(row=4, column=1)
    generate_button.grid(row=5, column=0, columnspan=2)
    self.password_field.grid(row=6, column=0, columnspan=2)

  def generatePassword(self):
    # Get the input from the user
    length = int(self.length_field.get())
    uppercase = self.uppercase_var.get()
    lowercase = self.lowercase_var.get()
    numbers = self.numbers_var.get()
    symbols = self.symbols_var.get()

    # Set of characters to choose from
    chars = ""
    if uppercase:
      chars += string.ascii_uppercase
    if lowercase:
      chars += string.ascii_lowercase
    if numbers:
      chars += string.digits
    if symbols:
      chars += string.punctuation

    # Generate the password
    password = ""
    for i in range(length):
      password += random.choice(chars)

    # Set the password in the password field
    self.password_field.delete(0, "end")
    self.password_field.insert(0, password)

if __name__ == "__main__":
  app = PasswordGenerator()
  app.mainloop()
