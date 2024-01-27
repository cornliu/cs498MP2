import subprocess
from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Start the stress_cpu.py script as a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "CPU stress test initiated.", 202

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address of the EC2 instance
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the server on port 5000
