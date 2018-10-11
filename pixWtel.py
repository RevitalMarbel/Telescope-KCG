from dronekit import connect
import latLonToYawPich
import Telconnect
#import serial
# Connect to the Vehicle (in this case a UDP endpoint)
lat1=0
lat2=0
lon1=0
lon2=0
alt1=0
alt2=0
vehicle = connect('COM4', wait_ready=True)  #'115200'
telescope=Telconnect.Telcontrol()
pich, yaw=latLonToYawPich.computeYawPich(lat1,lon1,alt1,lat2,lon2,alt2)
print("directing to"  ,pich, yaw)

def moveTelescope(yaw, pitch):
    if(abs(vehicle.attitude.yaw -yaw) < 1  or abs(vehicle.attitude.pitch -pitch) ):
    #move left right
        while(yaw > (vehicle.attitude.yaw- const)):
                telescope.manualRight();
                print("yaw" ,vehicle.attitude.yaw)
                print("right")
        while (yaw < (vehicle.attitude.yaw + const)):
                telescope.manualLeft();
                print("yaw", vehicle.attitude.yaw)
                print("left")
        while (pitch < (vehicle.attitude.pitch - const)):
                    telescope.manualUp();
                    print("alt", vehicle.attitude.pitch)
                    print("up")
        while (pitch > (vehicle.attitude.pitch + const)):
                    telescope.manualDown();
                    print("alt", vehicle.attitude.pitch)
                    print("down")
    else:
        print("value is to large",vehicle.attitude.pitch,vehicle.attitude.yaw )

const=0.01
int =0;


# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print "yaw %s"  %vehicle.attitude.yaw
print "pitch %s"  %vehicle.attitude.pitch
print "tel %s" %telescope.threshx
# Close vehicle object before exiting script
moveTelescope(1,0.7)
print("final" ,"alt", vehicle.attitude.pitch,"yaw", vehicle.attitude.yaw )

vehicle.close()

