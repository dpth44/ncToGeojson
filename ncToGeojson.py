import os
import netCDF4 as nc

currentSpace = os.getcwd()
geojsonObj = {"type": "FeatureCollection",
                   "features": []}

rootgrp = nc.Dataset("./data/in/20030101.nc")
lat = rootgrp.variables['lat'][:]
lon = rootgrp.variables['lon'][:]
chla = rootgrp.variables['chlorophyll_a']
spm = rootgrp.variables['suspended_matters'][:]
turbidity = rootgrp.variables['turbidity'][:]
# columns = ["latitude", "longitude", "chlorophyll_a",
#            "suspended_matters", "turbidity"]


for i in range(len(lat)):
    for k in range(len(lon)):
        featureObj = {"geometry": {"type": "Point",
                                   "coordinates": [lon[k], lat[i]]}, "properties": {"chlorophyll_a": chla[0][i]
                                                                                    [k], "suspended_matters": spm[0][i][k], "turbidty": turbidity[0][i][k]}}

        geojsonObj['features'].append(featureObj)

with open ("./data/out/myFile.geojson","w") as f:
    geojsonStr = str(geojsonObj)
    geojsonStr = geojsonStr.replace("'","\"")
    geojsonStr = geojsonStr.replace("masked","null")
    f.write(geojsonStr)
    f.close()
