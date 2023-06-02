import numpy as np

#this function converts hour minute second format to decimal degree format
def hms2dec(hr, m, s):
    if hr>=0 and hr<=24:
        return 15*(hr+m/60+s/3600)
    elif hr<0:
        return -15*(-hr+m/60+s/3600)

#this function converts hour minute second format to decimal degree format
def dms2dec(d, m, s):
    if d>=0:
        return (d+m/60+s/3600)
    elif d<0:
        return -(-d+m/60+s/3600)

"""
this function measures the angular distance between two celestial objects

parameters: 
right ascension of object 1, declination of object 1
right ascension of object 2, declination of object 2 

inputs are taken in degrees and output in degrees

This is also called the Haversine formula
"""

def angular_dist(ra1, dec1, ra2, dec2):
    ra1 = np.radians(ra1)
    ra2 = np.radians(ra2)
    dec1 = np.radians(dec1)
    dec2 = np.radians(dec2)
    
    a = np.sin(np.abs(dec1 - dec2)/2)**2
    b = np.cos(dec1)*np.cos(dec2)*np.sin(np.abs(ra1 - ra2)/2)**2
    return 2*np.arcsin(np.sqrt(a + b))*180/np.pi

if __name__ == '__main__':
  print(angular_dist(21.07, 0.1, 21.15, 8.2))
  print(angular_dist(10.3, -3, 24.3, -29))
