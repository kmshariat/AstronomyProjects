def hms2deg(hr, m, s):
    if hr>=0:
        return (hr+m/60+s/3600)
    elif hr<0:
        return -(-hr+m/60+s/3600)
    
if __name__=='__main__':
    hms2deg(73,21,14.4)
    hms2deg(-5,31,12)
