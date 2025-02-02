# Import necessary libraries for GUI, time handling, and sound
from tkinter import *
import datetime
import time
import winsound

def start_alarm(alarm_time):
    """
    Continuously checks the current time against the set alarm time.
    Plays a sound when the alarm time is reached.
    """
    while True:
        time.sleep(1)  # Pause for 1 second to avoid excessive CPU usage
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get current date
        
        print(f"Current Date: {current_date}")
        print(f"Current Time: {current_time}")

        if current_time == alarm_time:  # Check if it's time to wake up
            print("Wake up! Alarm is ringing...")
            winsound.PlaySound("alarm_sound.wav", winsound.SND_ASYNC)  # Play sound asynchronously
            break  # Exit the loop once the alarm rings

def get_alarm_time():
    """
    Retrieves user input from GUI fields and formats it into HH:MM:SS format.
    Calls start_alarm() to begin the alarm check.
    """
    alarm_time = f"{hour_var.get()}:{minute_var.get()}:{second_var.get()}"
    start_alarm(alarm_time)

# Initialize the main application window
app = Tk()
app.title("Alarm Clock")  # Window title
app.geometry("400x200")  # Set window size

# Instruction labels
Label(app, text="Enter time in 24-hour format!", fg="red", font="Arial").place(x=60, y=120)
Label(app, text="Hour   Min   Sec", font=("Arial", 10)).place(x=110, y=10)
Label(app, text="Set Alarm Time:", fg="blue", font=("Helvetica", 10, "bold")).place(x=10, y=35)

# Variables to store user input
hour_var = StringVar()
minute_var = StringVar()
second_var = StringVar()

# Input fields for hour, minute, and second
Entry(app, textvariable=hour_var, width=5).place(x=110, y=40)
Entry(app, textvariable=minute_var, width=5).place(x=150, y=40)
Entry(app, textvariable=second_var, width=5).place(x=190, y=40)

# Button to set the alarm
Button(app, text="Set Alarm", fg="red", width=10, command=get_alarm_time).place(x=110, y=80)

# Run the GUI application
app.mainloop()
