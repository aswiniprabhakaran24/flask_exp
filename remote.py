import serial
from flask import Flask, render_template, request
import time

app = Flask(__name__)

def send_hex(hex_number, ser):
    hex_bytes = bytes.fromhex(hex_number)
    ser.write(hex_bytes)
    print("Sent:", hex_number)

def receive_hex(ser):
    received_bytes = ser.read_all()
    hex_number = received_bytes.hex()
    return hex_number

@app.route('/remo', methods=['GET'])
def send_data():
    return render_template('remo.html')

@app.route('/wel', methods=['POST'])
def receive_data():
    hex_number=request.form['hex_data'] 
    print(hex_number)
    ser = serial.Serial('COM2',9600)
    time.sleep(1)
    hex_to_send = hex_number
    send_hex(hex_to_send, ser)
    time.sleep(0.5)
    received_hex = receive_hex(ser)
    print("Received:",(receive_hex))
    # for i in range(0, len(received_hex), 2):
        # print("Index {}: {}".format(i//2 + 1, received_hex[i:i+2]))
    ser.close()
    return render_template('wel.html', received_hex=received_hex)
    

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print("\nExiting...")


         
        