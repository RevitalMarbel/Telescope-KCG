import codecs

import binascii
import serial
boundrate=9600
myport= 'COM14'
const= 16777216

def angToDEC(ang):
    x=(const/360)*ang
    print (int(x))
    x=int(x)
    x=str(x)
    #y=hex(int(x))
    y =hex(int(x))[2:]
    y=text_to_bits("b"+y)
    #y=bin(int.from_bytes(y.encode(), 'big'))
    #y='b'+y
    #y=y.encode("hex")
    #y=binascii.hexlify(y)
    #y= format(y, 'x')
    # f=ord('b')
    # print (y[0])
    # f=codecs.decode('b'+y, "hex")
    #y=x.decode("hex")
    print(y)


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def serial_write():
    ser = serial.Serial(
        #port='/dev/ttyCOM14',
        port= myport,
        baudrate=boundrate,
        stopbits=serial.STOPBITS_ONE,
    )
    ser.write(b'01100010 00110010 00110000 00110000 00110000 00110000 00110000 00110000 00110000 00101100 00110000 00110000 00110000 00110000 00110000 00110000 00110000 00110000')

print (angToDEC(180))
serial_write()