import serial
from flask import Flask, render_template, request
from flask_cors import CORS 
import time

app = Flask(__name__)
CORS(app)  
def send_hex(hex_number, ser):
    hex_bytes = bytes.fromhex(hex_number)
    ser.write(hex_bytes)
    print("Sent:", hex_number)

def receive_hex(ser):
    received_bytes = ser.read_all()
    hex_number = received_bytes.hex()
    return hex_number

@app.route('/up')
def index():
    return "Javascript"
       
@app.route('/remo', methods=['GET','POST'])
def send_data():
    if request.method == 'POST':
        ser = serial.Serial('COM2', 9600)
        hex_number = request.form['hex_data'] 
        print(hex_number)
        time.sleep(1)
        hex_to_send = hex_number
        send_hex(hex_to_send, ser)
        time.sleep(0.5)
        received_hex = receive_hex(ser)
        print("Received:", received_hex)
        ser.close()
        return render_template('remo.html', received_hex=received_hex)
    return render_template('remo.html')

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nExiting...")
