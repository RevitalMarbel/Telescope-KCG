import telescopetracker

boundrate=9600
telPort= 'COM11'
loraPort= 'COM9'
br=9600
const= 16777216
timeToSleep=2
#Binyan 3
myLat=32.1039659
myLon=35.2095336
myAlt=698.2


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




def test_lora():
    res =telescopetracker.get_lora()
    print (res)

def test_telescope_lat_lon(lat, lon,alt):

    #yaw, pich = telescopetracker.computeYawPich(myLat, myLon, myAlt, 32.1101009, 35.1207510, 700)
    yaw, pich = telescopetracker.computeYawPich(myLat, myLon, myAlt, lat,lon,alt)
    azimut= telescopetracker.angToDEC(pich)
    alt=telescopetracker.angToDEC(yaw)

    telescopetracker.serial_write(azimut,alt)


def test_telescope_yaw_pich(yaw,pich):

    #yaw, pich = telescopetracker.computeYawPich(myLat, myLon, myAlt, 32.1101009, 35.1207510, 700)
    #yaw, pich = telescopetracker.computeYawPich(myLat, myLon, myAlt, lat,lon,alt)
    azimut= telescopetracker.angToDEC(pich)
    alt=telescopetracker.angToDEC(yaw)

    telescopetracker.serial_write(azimut,alt)

def set_te_to_zero():
    azimut = telescopetracker.angToDEC(0)
    alt = telescopetracker.angToDEC(0)

    telescopetracker.serial_write(azimut, alt)

def calibration(lat ,lon , alt):
    res= telescopetracker.computeYawPich(telescopetracker.myLat, telescopetracker.myLon, telescopetracker.myAlt,lat, lon , alt )
    print (res)
    return res

#main
# test_lora()
# test_telescope_lat_lon()
test_telescope_yaw_pich(292.9382, 0)
# set_te_to_zero()
#calibration( 32.104831,  35.214407, 685)