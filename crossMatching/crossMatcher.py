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

#testing
if __name__=='__main__':
    print(hms2dec(23,12,6))
    print(dms2dec(73,21,14.4))
    print(dms2dec(-5,31,12))
    print(dms2dec(22, 57, 18))
    print(dms2dec(-66, 5, 5.1))
