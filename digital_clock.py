import tkinter as tk
from time import strftime

# Create window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("500x250")
window.configure(bg="black")
window.resizable(False, False)

# Function to update time
def update_time():
    current_time = strftime("%I:%M:%S %p")
    current_date = strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    time_label.after(1000, update_time)

# Time Label
time_label = tk.Label(
    window,
    font=("Arial", 40, "bold"),
    bg="black",
    fg="cyan"
)
time_label.pack(pady=20)

# Date Label
date_label = tk.Label(
    window,
    font=("Arial", 18),
    bg="black",
    fg="white"
)
date_label.pack()

update_time()

window.mainloop()