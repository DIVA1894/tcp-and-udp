# app.py (Flask Backend)

from flask import Flask, request, render_template
import os
from client import send_file_to_server  # Import the client code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_file', methods=['POST'])
def send_file():
    server_ip = request.form['server_ip']
    protocol = request.form['protocol']
    file = request.files['file']
    
    # Save file temporarily
    file_path = os.path.join('uploads', file.filename)
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    file.save(file_path)

    # Call the client function to send the file
    send_file_to_server(file_path, server_ip, protocol)

    # Clean up the uploaded file
    os.remove(file_path)

    return f"File sent to {server_ip} using {protocol} protocol"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
