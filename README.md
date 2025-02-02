Refactored Code:
python
Copy
Edit
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
README.md
markdown
Copy
Edit
# Alarm Clock using Python 🕰️

This is a simple alarm clock application built using Python and Tkinter. The program allows users to set an alarm, which will ring at the specified time.

## Features
- Simple and easy-to-use GUI.
- Allows users to set an alarm in `HH:MM:SS` format.
- Uses `winsound` to play an alarm tone when the time is reached.

## Requirements
- Python 3.x
- Required Libraries:
  - `tkinter` (for GUI)
  - `datetime` (for handling time)
  - `time` (for delays)
  - `winsound` (for playing alarm sound on Windows)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alarm-clock.git
Navigate to the project folder:
bash
Copy
Edit
cd alarm-clock
Run the script:
bash
Copy
Edit
python alarm_clock.py
Usage
Enter the time in 24-hour format (HH:MM:SS).
Click the Set Alarm button.
The alarm will ring when the time matches the system time.
Example
If you want to set an alarm for 14:30:00, enter:

makefile
Copy
Edit
Hour: 14
Minute: 30
Second: 00
Notes
Ensure that the alarm_sound.wav file is present in the same directory.
This program currently supports Windows only due to the winsound module.
License
This project is open-source and available under the MIT License.

yaml
Copy
Edit

---

This refactored code improves readability, optimizes function names, and organizes variables better. The `README.md` provides clear instructions for users to set up and use the alarm clock. Let me know if you need any modifications!






