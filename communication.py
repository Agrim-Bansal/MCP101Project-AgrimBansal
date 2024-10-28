import serial
import time
import atexit

serialaddress = input('usbModem : ')
SerialObj = serial.Serial(serialaddress)         # COMxx  format on Windows
                                                        # ttyUSBx format on Linux
SerialObj.baudrate = 9600                               # set Baud rate to 9600
SerialObj.bytesize = 8                                  # Number of data bits = 8
SerialObj.parity  ='N'                                  # No parity
# SerialObj.stopbits = 1                                  # Number of Stop bits = 1
# time.sleep(3)
                                                        # SerialObj.write(b'A')    #transmit 'A' (8bit) to micro/Arduino

def send_message(message):
    global SerialObj
    try:
        SerialObj.write(bytes(message, 'utf8'))
    except Exception as e:
        if str(e) == "write failed: [Errno 6] Device not configured":
            time.sleep(1)
            SerialObj = serial.Serial(serialaddress)
        else:
            print("Error in sending message : ", e)
        
    time.sleep(1)
            
# def exit_handler():
#     SerialObj.close()      
# atexit.register(exit_handler)



if __name__ == "__main__":
    try : 
        while True:
            send_message(input("Message to send : "))
            # SerialObj.write(bytes(input('Message to send : '), 'utf8'))    #transmit 'A' (8bit) to micro/Arduino
    except KeyboardInterrupt:
        print("Exiting the program")
        SerialObj.close()      # Close the port
# SerialObj.write(input('Message to send : '))    #transmit 'A' (8bit) to micro/Arduino
# SerialObj.close()      # Close the port