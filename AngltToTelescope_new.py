import codecs

import binascii
import serial
import time
boundrate=9600
myport= 'COM21'
const= 16777216

def angToDEC(ang):
    if(ang==0):
        return '00000000'
    x=(const/360)*ang
    #print (int(x))
    x=int(x)
    x=str(x)
    #y=hex(int(x))
    y =hex(int(x))[2:]
    #y=text_to_bits("b"+y)
    #y=bin(int.from_bytes(y.encode(), 'big'))
    #y='b'+y
    #y=y.encode("hex")
    #y=binascii.hexlify(y)
    #y= format(y, 'x')
    # f=ord('b')
    # print (y[0])
    # f=codecs.decode('b'+y, "hex")
    #y=x.decode("hex")
    y=y + '00'
    if(len(y)<8):
        y='0'+y
    print(y)
    return (y)


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def serial_write(a1,a2):
    ser = serial.Serial(
        #port='/dev/ttyCOM14',
        port= myport,
        baudrate=boundrate,
        stopbits=serial.STOPBITS_ONE
    )
    time.sleep(2)

    #a1 = 40000000
    #a2 = '00000000'

    to_send = "b"+str(a1)+","+str(a2)#+"b"
    print(to_send)

    ser.write(to_send.encode())

    #input1=str.encode('01100010 00110010 00110000 00110000 00110000 00110000 00110000 00110000 00110000 00101100 00110000 00110000 00110000 00110000 00110000 00110000 00110000 00110000')
    #print(type(input1))
    #print(input1)
    #input= ('01100010 00110010 00110000 00110000 00110000 00110000 00110000 00110000 00110000 00101100 00110000 00110000 00110000 00110000 00110000 00110000 00110000 00110000')
    #ser.write(input1)
    #ser.write(input)
    #ser.write(chr(62) chr(34) chr(300) chr(30) chr(30) chr(30) chr(30) chr(30) chr(30) chr(2c) chr(30) chr(30) chr(30) chr(30) chr(30) chr(30) chr(30) chr(30) chr(62))

azimut= angToDEC(0)
alt=angToDEC(0)

serial_write(azimut,alt)
#serial_write()