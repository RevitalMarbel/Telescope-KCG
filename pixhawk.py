from dronekit import connect
import Telconnect
#import serial
# Connect to the Vehicle (in this case a UDP endpoint)
vehicle = connect('COM3', wait_ready=True)  #'115200'

const=1


# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print "yaw %s"  %vehicle.attitude.yaw
print "alt %s"  %vehicle.attitude.pitch
# Close vehicle object before exiting script
vehicle.close()

