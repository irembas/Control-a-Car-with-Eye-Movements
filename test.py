import serial  # import the serial library

# add the following lines to initialize the serial connection
bluetoothSerial = serial.Serial(port="COM8", baudrate=9600)
bluetoothSerial.flushInput()
bluetoothSerial.close()
bluetoothSerial.open()

# define the commands that will be sent to the Arduino
CMD_LEFT = "left"
CMD_RIGHT = "right"
CMD_FORWARD = "forward"
CMD_STOP = "stop"

while True:
    # get user input for the command to send to the Arduino
    user_input = input("Enter a command (left, right, forward, stop): ")

    # send the command to the Arduino
    bluetoothSerial.write(user_input.encode())

    # check if the user wants to exit the program
    if user_input == "exit":
        break

# close the serial connection
bluetoothSerial.close()