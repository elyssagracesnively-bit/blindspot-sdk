import serial
import subprocess
import sys
print(sys.version)   # confirms correct python version (3.10.13)
robot_ip = "192.168.80.3"

if __name__ == "__main__":
    temporary = 0;
    
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.reset_input_buffer()
    print("Sum of every number up to:")
    
    while True:
        if ser.in_waiting > 0:
            value = int(ser.readline().decode('utf-8').rstrip())
            if value == 0:
                temporary = 0;
            temporary += value;
            print(f"{value}: {temporary}")
            if value >= 1:
                print("CHECK")
                subprocess.run(["python","square_walk.py",robot_ip])
