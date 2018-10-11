import math


pich=0
yaw=0

def computeYawPich(lat1 ,lon1, alt1, lat2,lon2,alt2):
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
    return [pich, yaw]