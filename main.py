#Andrew Ribar
#11-1-2023
#System Resource Monitor

import psutil
import time
import tkinter as tk

# Set resource thresholds
cpu_threshold = 90  # 90% CPU usage
memory_threshold = 80  # 80% memory usage
disk_threshold = 90  # 90% disk usage

# Create the GUI window
root = tk.Tk()
root.title("System Resource Monitor")

# Create labels to display resource usage and alerts
cpu_label = tk.Label(root, text="", font=("Helvetica", 12))
memory_label = tk.Label(root, text="", font=("Helvetica", 12))
disk_label = tk.Label(root, text="", font=("Helvetica", 12))
alert_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), fg="red")

# Arrange the labels in the GUI window
cpu_label.pack()
memory_label.pack()
disk_label.pack()
alert_label.pack()


# Function to update the GUI labels
def update_gui():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Update the GUI labels with resource usage information
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    memory_label.config(text=f"Memory Usage: {memory_usage}%")
    disk_label.config(text=f"Disk Usage: {disk_usage}%")

    # Check for resource threshold breaches and display alerts
    alert_text = ""
    if cpu_usage > cpu_threshold:
        alert_text += f"High CPU usage detected: {cpu_usage}%\n"

    if memory_usage > memory_threshold:
        alert_text += f"High memory usage detected: {memory_usage}%\n"

    if disk_usage > disk_threshold:
        alert_text += f"High disk usage detected: {disk_usage}%"

    alert_label.config(text=alert_text)

    # Schedule the function to run again after a delay
    root.after(2000, update_gui)  # 2000 ms = 2 seconds (adjust the delay as needed)


# Start the resource monitoring and GUI update function
update_gui()

# Run the GUI application
root.mainloop()



