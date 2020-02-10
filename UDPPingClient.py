# Blombach, Chicas-Terrill, Orduna, Stephens
from socket import *
from statistics import mean
import time


def rtt_equation(sample_arr):
    """
    Calculates and displays the RTT Average, Max, and Min
    :param sample_arr: List of Samples
    :return:
    """

    estimated_rtt = 0
    dev_rtt = 0
    alpha = 0.125
    beta = 0.25

    print("========================")

    for sampleRTT in sample_arr:
        estimated_rtt = (1 - alpha) * estimated_rtt + alpha * sampleRTT
        dev_rtt = (1 - beta) * dev_rtt + beta * abs(sampleRTT - estimated_rtt)
    print('estimated_rtt: ', round(estimated_rtt, 3))
    print("dev_rtt: ", round(dev_rtt, 3))
    print("========================")
    timeout_interval = estimated_rtt + 4 * dev_rtt
    print('TimeoutInterval: ', round(timeout_interval, 3))


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# set timeout for response
clientSocket.settimeout(1)

samples_list = []
sent = 10

for ping in range(sent):
    try:
        # Message sent to ping the server
        message = f"This is Ping {ping + 1} {time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())}"

        # Starting time
        t = time.time()

        # Setup the socket and send the message
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # Receive the response from the server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())

        # Calculate the elapsed time from when ping was sent
        elapsed_time = (time.time() - t) * 1000

        # Check if ping is returned, if not, print error
        if elapsed_time:
            samples_list.append(elapsed_time)
        print(f"RTT is {round(elapsed_time, 3)}ms")
    except timeout as e:
        print("Request timed out")
clientSocket.close()

sent = 10
received = len(samples_list)
lost = 10 - len(samples_list)
loss_percentage = (lost/10.) * 100

max_rtt = round(max(samples_list), 3)
min_rtt = round(min(samples_list), 3)
avg_rtt = round(mean(samples_list), 3)

print("=======================================================")
print(f"Ping statistics for {serverAddress}: Packets: Sent = {sent}, Received = {received}, Lost = {lost}, "
      f"Loss Percentage = {loss_percentage}% \nApproximate round trip "
      f"times in milli-seconds: Minimum = {min_rtt}ms, Maximum = {max_rtt}ms, Average = {avg_rtt}ms")

# Display all the rtt values
rtt_equation(samples_list)

