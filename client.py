import socket

client_socket = socket.socket()
port = 12345
client_socket.connect(('172.16.2.238',port))

#recieve connection message from server
recv_msg = client_socket.recv(1024)
print (recv_msg)

#send user details to server. 
# Enter the username with a ‘#’ prefix. Example: #alice
send_msg = str(input("Enter your user name(prefix with #):"))
client_socket.send(send_msg)


#receive and send message from/to different user/s

while True:
    recv_msg = client_socket.recv(1024)
    print (recv_msg)
    #Now, send the message to a user by following the format @username:message. 
    # Example: @bob:Hello, Bob! This is alice
    send_msg = input("Send your message in format [@user:message] ")
    if send_msg == 'exit':
        break;
    else:
        client_socket.send(send_msg)

client_socket.close()