import socket
import subprocess
import random
from io import BytesIO

## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()

## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

def test_curl_request(url):
    url = "http://" + ip_address
    # Define the command to execute using curl
    command = ['curl', url]

    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Return the stdout of the curl command
    return result.stdout

def test_curl_request_env(url):
    url = "http://" + ip_address + "/env"
    # Define the command to execute using curl
    command = ['curl', url]

    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Return the stdout of the curl command
    return result.stdout

def test_curl_request_int(url):
    url = "http://" + ip_address + "/" + str(random.randint(0,100))
    # Define the command to execute using curl
    command = ['curl', url]

    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    result = result.decode('utf-8')
    # Return the stdout of the curl command
    return result.stdout

# Make a curl request to the RNG app
response = test_curl_request(ip_address)
print(response)
response = test_curl_request_env(ip_address)
print(response)
#response = test_curl_request_int(ip_address)
#print(response)