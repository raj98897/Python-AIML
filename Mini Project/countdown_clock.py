import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
# Note: winsound and win10toast are Windows-only libraries
try:
    import winsound
    from win10toast import ToastNotifier
except ImportError:
    winsound = None
    ToastNotifier = None

def countdown():
    try:
        # Convert input values to total seconds
        h = int(hour.get() or 0)
        m = int(minus.get() or 0)
        s = int(secon.get() or 0)
        t = h * 3600 + m * 60 + s
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values")
        return

    while t > -1:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        
        # Update the display label instead of creating new ones
        display = f"{hours:02d}:{mins:02d}:{secs:02d}"
        timer_display.config(text=display)
        
        window.update()
        time.sleep(1)
        t -= 1
    
    # Logic for when time is up
    timer_display.config(text="00:00:00")
    messagebox.showinfo("Time-Up", "The countdown has finished!")
    
    if check.get() and winsound:
        winsound.Beep(440, 1000)
    
    if ToastNotifier:
        toast = ToastNotifier()
        toast.show_toast("Notification", "Timer is Off", duration=5, threaded=True)

# Main Window Setup
window = tk.Tk()
window.geometry('400x500')
window.title('Countdown Clock')

# Defining Tkinter variables
hour = tk.StringVar(value="00")
minus = tk.StringVar(value="00")
secon = tk.StringVar(value="00")
check = tk.BooleanVar()

# UI Elements
tk.Label(window, text="Countdown Clock and Timer", font=('Calibri', 15)).pack(pady=20)

# Real-time clock display
current_time_lbl = tk.Label(window, text=datetime.now().strftime("%H:%M:%S"))
current_time_lbl.pack()

tk.Label(window, text="Enter time (HH : MM : SS)", font=('bold', 10)).pack(pady=10)
frame = tk.Frame(window)
frame.pack()

tk.Entry(frame, textvariable=hour, width=3, font=("Arial", 18)).pack(side=tk.LEFT)
tk.Entry(frame, textvariable=minus, width=3, font=("Arial", 18)).pack(side=tk.LEFT)
tk.Entry(frame, textvariable=secon, width=3, font=("Arial", 18)).pack(side=tk.LEFT)

# Timer Display Label
timer_display = tk.Label(window, text="00:00:00", font=("Arial", 24), fg="red")
timer_display.pack(pady=20)

tk.Checkbutton(window, text='Enable Beep at End', variable=check).pack()
tk.Button(window, text="Start Countdown", command=countdown, bg='yellow', width=15).pack(pady=20)

window.mainloop()
