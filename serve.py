from flask import Flask, request, render_template
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'Running stress_cpu.py'

@app.route('/', methods=['GET'])
def get_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
