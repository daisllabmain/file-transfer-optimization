import socket
import time

# Server address (replace with the actual server IP or hostname)
SERVER_ADDRESS = ("129.114.108.66", 22)

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start measuring time
start_time = time.time()

# Connect to the server
sock.connect(SERVER_ADDRESS)

# Send a simple message (e.g., an HTTP GET request)
sock.sendall(b"GET / HTTP/1.1\r\nHost: 129.114.108.66\r\n\r\n")

# Receive some data from the server (just the header is enough)
data = sock.recv(1024)

# Close the socket
sock.close()

# End measuring time
end_time = time.time()

# Calculate RTT
rtt = end_time - start_time
formatted_rtt = f"{rtt:.3f}"
print("RTT:", formatted_rtt, "seconds")
