# coding: utf-8   
  
from flask import Flask 
import serial
import time
import json  
import datetime   

DEV_PATH = "/dev/ttyAMA0"
PORT = 5000

app = Flask(__name__)

class Sensor():
    PACKET = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]
    ZERO = [0xff, 0x01, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78]
    
    def __init__(self, ser):
        self.serial = serial.Serial(ser, 9600, timeout=1)
        time.sleep(1)

    def do_zero_calibration(self):
        #self.serial.write(bytearray(Sensor.ZERO))
        return {                                                                                                                                                                                                                                                                                                           
            "ppm": 0,                                                                                                                                                                                                                                                                                
            "msg": "Done zero calibration",                                                                                                                                                                                                                                                                                           
            "time": datetime.datetime.today().isoformat(),                                                                                                                                                                                                                                                                 
        }

    def get_co2_ppm(self):
        self.serial.write(bytearray(Sensor.PACKET))  
        res = self.serial.read(size=9)  
        res = bytearray(res) 
        checksum = 0xff & (~(res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]) + 1)

        if res[8] == checksum:  
            return { 
                "ppm": (res[2] << 8) | res[3],
                "msg": "Get CO2 ppm",
                "time": datetime.datetime.today().isoformat(),  
            }
        else:
            raise Exception("checksum: " + hex(checksum))    

    def close(self):
        self.serial.close()

@app.route('/', methods=["GET"])
def get_co2():
    co2 = Sensor(DEV_PATH)
    result = co2.get_co2_ppm()
    return result

@app.route('/calibration', methods=["POST"])    
def run_calibration():   
    co2 = Sensor(DEV_PATH)    
    result = co2.do_zero_calibration()    
    return result 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
