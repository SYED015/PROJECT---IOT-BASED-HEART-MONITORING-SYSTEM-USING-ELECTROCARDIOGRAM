import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Configure Serial Port (Change 'COM9' to your Arduino's port)
ser = serial.Serial('COM3', 9600)  # Replace with the correct COM port

# Set up plot
fig, ax = plt.subplots()
ax.set_ylim(200, 500)  # ECG output range
ax.set_title("Real-Time ECG Monitoring")
ax.set_xlabel("Time")
ax.set_ylabel("ECG Signal")

data = deque([0] * 100, maxlen=100)  # Store last 100 readings
line, = ax.plot(data, color='blue')

# Update function for animation
def update(frame):
    if ser.in_waiting > 0:
        try:
            ecg_value = int(ser.readline().decode().strip().split(" ")[-1])  # Read last value
            data.append(ecg_value)
            line.set_ydata(data)
        except:
            pass
    return line,

# Run animation
ani = animation.FuncAnimation(fig, update, interval=50, blit=True, cache_frame_data=False)
plt.show()

# Close serial connection on exit
ser.close()
