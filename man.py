import serial
from flask import Flask, request, Response, render_template, jsonify
from flask_cors import CORS
import time
import json

app = Flask(__name__)
CORS(app)
parsed_data = {}

def send_hex(hex_number, ser):
    hex_bytes = bytes.fromhex(hex_number)
    ser.write(hex_bytes)
    print("Sent:", hex_number)

def receive_hex(ser):
    received_bytes = ser.read_all()
    return received_bytes

def parse_received_data(received_bytes, hex_num):
   
    try:
        received_hex = received_bytes.hex()
        print("Received hex:", received_hex)
        if hex_num == "0102040605":
            parsed_data['Channel'] = received_bytes[3]
            parsed_data['Sync Address'] = received_bytes[7]
            parsed_data['Destination Address'] = received_bytes[13]
            parsed_data['Source Address'] = received_bytes[15]
            parsed_data['Standby Time'] = received_bytes[11]
            parsed_data['Transmitter Power'] = received_bytes[9]
        elif hex_num == "0102041109":
            parsed_data['Combo First Key'] = received_bytes[7]
            parsed_data['Combo Second Key'] = received_bytes[5]
            parsed_data['Combo Secure'] = received_bytes[3]
        elif hex_num == "0102040F08":
            parsed_data['Low battery v'] = received_bytes[3]
        else:
            print("Some error occured")
            
    except Exception as e:
        print("Error parsing received data:", e)
    return parsed_data

@app.route('/up')
def index():
    try:
        ser = serial.Serial('COM2', 9600) 
        hex_number = '0102040605' 
        
        hex_list = ["0102041109", "0102040F08", "0102040605", "010204000C", "010206014E4F4D"]
        for hex_value in hex_list:
            print( hex_value)
        
            if 'hex_data' in request.args:
                hex_number = request.args['hex_data']
            print("Hex number:", hex_number)
            # time.sleep(1)
            hex_to_send = hex_value
            send_hex(hex_to_send, ser)
            time.sleep(0.5)
            received_hex = receive_hex(ser)
            print("Received:", received_hex)
        
            parsed_data = parse_received_data(received_hex, hex_value)
        # parsed_data = "test ok"
        ser.close()
        
        
        return jsonify(parsed_data)
        
    except serial.SerialException as e:
        print("Serial port error:", e)
        return "Error: Serial port not available"
    except Exception as e:
        print("Error:", e)
        return "Error: Something went wrong"

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nExiting...")
