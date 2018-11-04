import latLonToYawPich
#barkan
pich, yaw=latLonToYawPich.computeYawPich(32.103153,35.209495,698.2,32.107624,35.110586,449)

#moon
#pich, yaw=latLonToYawPich.computeYawPich(32.103153,35.209495,698.2,39.58560,104.89598,900)


print (pich, yaw)