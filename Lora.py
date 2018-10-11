import serial


class Lora():
    def __init__(self, port="COM6", baudrate="115200"):
        self.ser = serial.Serial(port, baudrate)  # need to check the com
       # self.connect()
        print("connected")
        while(True):
            msg=self.ser.readline()
            print (msg)
            #if (msg[0] == "g" ) :
               # print(self.ser.readline())


    def connect(self):
        if not self.ser.is_open:
            self.ser.open()

    def disconnect(self):
        if not self.ser.closed:
            self.ser.close()

