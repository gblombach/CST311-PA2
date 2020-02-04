#Blombach, Chicas-Terrill, Orduna, Stephens
from socket import *
from statistics import mean
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# set timeout for response
clientSocket.settimeout(1)

rtt_arr = []
sent = 10

for ping in range(sent):
    try:
        message = f"This is Ping {ping + 1} {time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())}"
        t = time.time()
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
        elapsed_time = (time.time() - t) * 1000
        if elapsed_time:
            rtt_arr.append(elapsed_time)
        print(f"RTT is {round(elapsed_time, 3)}ms")
    except timeout as e:
        print("Request timed out")
clientSocket.close()

sent = 10
received = len(rtt_arr)
lost = 10 - len(rtt_arr)
loss_percentage = (lost/10.) * 100

max_rtt = round(max(rtt_arr), 3)
min_rtt = round(min(rtt_arr), 3)
avg_rtt = round(mean(rtt_arr), 3)

print("=======================================================")
print(f"Ping statistics for {serverAddress}: Packets: Sent = {sent}, Received = {received}, Lost = {lost}, "
      f"Loss Percentage = {loss_percentage}% \nApproximate round trip "
      f"times in milli-seconds: Minimum = {min_rtt}ms, Maximum = {max_rtt}ms, Average = {avg_rtt}ms")
