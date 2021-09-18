import serial

ser = serial.Serial("/dev/barcode_reader", 115200, timeout=0.001)


while True:
    #print('hi')
    if ser.readable():
        res = ser.read()
        if res != b'':
            res += ser.readline()
            print(res.decode())
        
        