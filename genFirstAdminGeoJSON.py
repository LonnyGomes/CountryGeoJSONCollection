#!/usr/bin/python
import requests
import json
import os

inputFile="countries.geojson"
featureKey="ne_10m_adm"
outputPath = "./"
#shouldLint = 1
validate_endpoint = 'http://geojsonlint.com/validate'

fp = open(inputFile)
geoJSONList = fp.readlines()
fp.close

geoJSONData = json.loads(' '.join(geoJSONList))

geoFeatures = geoJSONData["features"]

for curFeature in geoFeatures:
    curProperties = curFeature["properties"]
    curKey = curProperties[featureKey]

    print "Creating geojson file for " + curKey

    curFilename = outputPath + curKey + ".geojson"

    if (os.path.exists(curFilename)):
        print "File already exists!"
        next
    
    curGeoDataStr = json.dumps(curFeature)
    #lint_request = requests.post(validate_endpoint, data=curGeoDataStr)
    #print lint_request.json()

    #save out to file
    fpo = open(curFilename, "w")
    fpo.write(curGeoDataStr)
    fpo.close()
