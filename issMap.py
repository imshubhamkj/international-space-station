# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:11:53 2019

@author: shubham kumar
"""

import requests
import json
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def getastronauts():
    ##getting astronauts details using api http://api.open-notify.org/astros.json
    r = requests.get(url='http://api.open-notify.org/astros.json')
    data = json.loads(r.content)
    A_names = []
    for each in data['people']:
        A_names.append(each['name'])
    return A_names

def getposition():

    ##getting astronauts details using api http://api.open-notify.org/iss-now.json
    r = requests.get(url='http://api.open-notify.org/iss-now.json')
    data = json.loads(r.content)

    return float(data['iss_position']['latitude']),float(data['iss_position']['longitude']),float(data['timestamp'])


def issPositionOnMap(s,lat, lon, i):

    m = Basemap(projection='robin',lon_0=-105,lat_0=40,resolution='l')
    m.drawcoastlines()
    m.fillcontinents(color='green',lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')
    
    #ploting astronauts location on base map.
    x, y = m(lon, lat)
    m.plot(x, y, color='red', marker='o')
    x2, y2 = m(lon+10,lat+10)  
    plt.annotate('iss', xy=(x, y),  xycoords='data',
                xytext=(x2, y2), textcoords='data',bbox=dict(boxstyle="round", alpha=0.8),
                arrowprops=dict(arrowstyle="fancy", color='b')
                )
    plt.title('International Space Station Positon')
    plt.xlabel('longitude:'+str(lon)+'  '+'latitude:'+str(lat))
    
    #address = 'z'+str(i)+'.png'
    
    #plt.savefig(address)
    plt.show(block=False)
    plt.pause(5)
    plt.close()
    


if __name__ == "__main__":
    print("List of Astronauts on space station\n",getastronauts())
    flag=True
    i=0
    while(flag):
        lat, lon,timestamp = getposition()
        print("\n")
        print("------map for timestamp",timestamp,"On the server------\n\n","position of International space station now \n ","latitude:",lat,"longitude:",lon)
        issPositionOnMap(getastronauts(),lat, lon, i)
        i=i+1
    
