import codecs

import binascii
import serial
import time
#import latLonToYawPich
import math
import time;  # This is required to include time module.

now = time.time()
import struct
boundrate=9600
telPort= 'COM13'
loraPort= 'COM9'
br=9600
const= 16777216
timeToSleep=2


#Binyan 3
myLat=32.10371
myLon=35.21128
myAlt=685
serTel = serial.Serial(
        #port='/dev/ttyCOM14',
        port= telPort,
        baudrate=boundrate,
        stopbits=serial.STOPBITS_ONE
    )

serLora = serial.Serial(
        # port='/dev/ttyCOM14',
        port=loraPort,
        baudrate=br,
        stopbits=serial.STOPBITS_ONE,
           timeout=5

    )
file = open('telescope_tracker %s .txt' %now , 'w')
file.write("mycoords: lat" + str(myLat) + "lon" + str(myLon) + " alt " + str(myAlt)+"\n")
#file.write("my coords mylat:"+ (str)myLat + "mylon:" + (str)myLon + "myalt" + (str)myAlt+"" )
# #Lab
# myLat=32.097763
# myLon=34.963255
# myAlt=688

lat=0
lon=0
alt=0

oldLat = lat
oldLon = lon
oldAlt = alt

# global lat
# global lon
# global alt
#
# lat= myLat
# lon= myLon
# alt= myAlt

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
    y = y + '00'
    if (len(y) < 6):
        y = '000' + y
    if( len(y)<7):
        y = '00' + y
    if(len(y)<8):
        y='0'+y
    print(y)
    return (y)


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def serial_write(a1,a2):

    time.sleep(2)

    #a1 = 40000000
    #a2 = '00000000'

    to_send = "b"+str(a1)+","+str(a2)+"b"
    print(to_send)

    serTel.write(to_send.encode())



def get_location():
    # ser = serial.Serial(
    #     # port='/dev/ttyCOM14',
    #     port=telPort,
    #     baudrate=boundrate,
    #     stopbits=serial.STOPBITS_ONE
    # )
    time.sleep(2)
    serTel.write("z".encode())
    time.sleep(10)
    line=serTel.read(18)

    print (line)


def get_lora():

    global oldLat
    global oldLon
    global oldAlt

    global lat
    global lon
    global alt

    mlat=None
    mlon=None
    myLat=None

    #time.sleep(2)
    #ser.write("z".encode())
    time.sleep(1)
    print("serial reqd begin")
    line=serLora.readline()
    print("line", line)
    res=line.decode("utf-8")
    print("res", res)
    res=res.split(",")
    #print("res" ,res)
    if res[0]=='gps':
        if(len(res)>1  and len(res[0])!= "" and  res[1] is not None ):
            try:
                mlat = float(res[1])
            except ValueError as e:
                print ("error", e, "on line", "mlat")
                mlat=lat

            print(mlat)
        else:
            print("lat not found")
            mlat=  lat

        if (len(res) > 2 and len(res[1])!= "" and  res[2] is not None):
            try:
                mlon = float(res[2])
            except ValueError as e:
                print("error", e, "on line", "mlon")
                mlon= lon
            print(mlon)
        else:
            print("lon not found")
            mlon = lon

        if (len(res) > 3 and len(res[2])!= "" and  res[3] is not None):
            try:
                malt = float(res[3])
            except ValueError as e:
                print("error", e, "on line", "malt")
                malt = lat
            print(malt)
        else:
            print("alt not found")
            malt = alt


        #res=struct.unpack('3f', line)
        #res=float(line.strip('\x00'))


    if(mlat is not None and mlon is not None and malt is not None):
        return mlat,mlon,malt
        print(mlat, mlon, malt)
    else:
        return lat ,lon, alt


def get_lora_old():

    global oldLat
    global oldLon
    global oldAlt

    global lat
    global lon
    global alt

    ser = serial.Serial(
        # port='/dev/ttyCOM14',
        port=loraPort,
        baudrate=br,
        stopbits=serial.STOPBITS_ONE,
           timeout=5

    )
    #time.sleep(2)
    #ser.write("z".encode())
    time.sleep(1)
    print("serial reqd begin")
    line=ser.readline()
    print("line", line)
    res=line.decode("utf-8")
    print("res", res)
    res=res.split(",")
    #print("res" ,res)
    #if res[0]=='gps':
    if(len(res)>0  and len(res[0])!= "" and  res[0] is not None ):
        try:
            mlat = float(res[0])
        except ValueError as e:
            print ("error", e, "on line", "mlat")
            mlat=lat

        print(mlat)
    else:
        print("lat not found")
        mlat=  lat


    if (len(res) > 1 and len(res[1])!= "" and  res[1] is not None):
        try:
            mlon = float(res[1])
        except ValueError as e:
            print("error", e, "on line", "mlon")
            mlon= lon
        print(mlon)
    else:
        print("lon not found")
        mlon = lon

    if (len(res) > 2 and len(res[2])!= "" and  res[2] is not None):
        try:
            malt = float(res[2])
        except ValueError as e:
            print("error", e, "on line", "malt")
            malt = lat
        print(malt)
    else:
        print("alt not found")
        malt = alt


    #res=struct.unpack('3f', line)
    #res=float(line.strip('\x00'))

    print (mlat, mlon,malt)
    return mlat,mlon,malt

def is_align():
    ser = serial.Serial(
        # port='/dev/ttyCOM14',
        port=telPort,
        baudrate=boundrate,
        stopbits=serial.STOPBITS_ONE
    )
    time.sleep(2)
    ser.write("J".encode())
    time.sleep(2)
    line = ser.read(1)
    print(line)

def test_string(str):
    ser = serial.Serial(
        # port='/dev/ttyCOM14',
        port=telPort,
        baudrate=boundrate,
        stopbits=serial.STOPBITS_ONE
    )
    time.sleep(2)
    ser.write(str.encode())

    print(str.encode())


def computeYawPich(lat1 ,lon1, alt1, lat2,lon2,alt2):
    print("lat lon from funtion", lat1 ,lon1, alt1, lat2,lon2,alt2)
    delLat=lat2-lat1
    delLon=lon2-lon1
    delAlt=alt2-alt1

    radDelLat=math.radians(delLat)
    delLatFromNorth=math.sin(radDelLat)*1000*6371

    lat2rad=math.radians(lat1)
    delLonInRad=math.radians(delLon)
    delFromEast=math.sin(delLonInRad)*6371*1000*math.cos(lat2rad)

    dxy=math.sqrt(delLatFromNorth*delLatFromNorth+delFromEast*delFromEast)

    pichInrad=math.atan2(delAlt,dxy )

    pichIndeg=math.degrees(pichInrad)
    yawInrad=math.atan2(delLatFromNorth,delFromEast)
    yawIndeg=math.degrees(yawInrad)
    yawFromNorth=90-yawIndeg
    if(yawFromNorth<0):
        yawFromNorth=yawFromNorth+360


    yaw=yawFromNorth
    pich=pichIndeg

    print("pich yaw from function" ,pich ,yaw)
    return [pich, yaw]


def main_loop():


    #print(lat, lon, alt)


    global oldLat
    global oldLon
    global oldAlt

    global lat
    global lon
    global alt

    global file
    oldLat = lat
    oldLon = lon
    oldAlt = alt
    lat, lon, alt = get_lora()
    t=time.time()
    file.write(str(t)+"\n")
    file.write("from lora: lat"+str(lat) +"lon"+ str(lon)+" alt "+str(alt)+"\n" )
    if (lat-30  <10  and lat-30  >0 and  lon-30  <10  and lon-30):


        if( lat == oldLat and   lon== oldLon and  alt==oldAlt):
            print("same coordinates")
        else:
            print("gps coords: ", lat, lon, alt)
            print("my coords: ", myLat, myLon, myAlt)

            yaw, pich = computeYawPich(myLat, myLon, myAlt, lat, lon, alt)

            print("pich yaw: ", pich, yaw)
            if (yaw < 0):
                yaw = 0
            azimut = angToDEC(pich)
            alt = angToDEC(yaw)

            serial_write(azimut, alt)
            #file.write("from lora: lat" + str(lat) + "lon" + str(lon) + " alt " + str(alt))
            file.write(" yaw :" +str(yaw)+ "pich :" +str(pich)+"\n" )
    else:
        print("bad coordinates", lat , lon )
        file.write("bad coordinates " +str(lat)+ " "+str(lon)+"\n" )
        global timeToSleep
    time.sleep(timeToSleep)

def move_to_angle(pich , yaw):
    #yaw, pich = computeYawPich(myLat, myLon, myAlt, 32.1101009, 35.1207510, 700)
    azimut = angToDEC(pich)
    alt = angToDEC(yaw)
    serial_write(azimut, alt)

#azimut= angToDEC(0.50)
#alt=angToDEC(0)

#serial_write(azimut,alt)
#serial_write()
#get_location()
#is_align()

#test_string("b00000000, 00000000")

#Main:

#32.102697, 35.210003
# yaw, pich = computeYawPich(myLat, myLon, myAlt, 32.1101009, 35.1207510, 700)
# azimut= angToDEC(pich)
# alt=angToDEC(yaw)
#
# serial_write(azimut,alt)

#
#
#

#from barkan:
#move_to_angle(85.336393, 0)
#move_to_angle(274.663606, 0)
#move_to_angle(0, 0)
def main():
    counter=0
    while counter < 20:
        main_loop()

if __name__=="__main__":
    #move_to_angle(0, 0)
    #move_to_angle(292.9382, 0)
    main()
    file.close()