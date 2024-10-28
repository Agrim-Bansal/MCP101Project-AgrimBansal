import communication
while True:
    message = input("Enter message to send : ")
    communication.send_message(message)
