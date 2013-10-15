#!/usr/bin/python
import requests
import json
import os

inputFile="countries.geojson"
featureKey="ne_10m_adm"
outputPath = "geojson"
#shouldLint = 1
validate_endpoint = 'http://geojsonlint.com/validate'

try:
    fp = open(inputFile)
    geoJSONList = fp.readlines()
    fp.close
except IOError:
    print "Could not open geojson file for reading:" + inputFile
    exit(-1)

geoJSONData = json.loads(' '.join(geoJSONList))

geoFeatures = geoJSONData["features"]

for curFeature in geoFeatures:
    curProperties = curFeature["properties"]
    curKey = curProperties[featureKey]

    print "Creating geojson file for " + curKey

    curFilename = outputPath + os.sep +  curKey + ".geojson"

    if (os.path.exists(curFilename)):
        print "File already exists!"
        next
    
    curGeoDataStr = json.dumps(curFeature)
    #lint_request = requests.post(validate_endpoint, data=curGeoDataStr)
    #print lint_request.json()

    #save out to file
    try:
        fpo = open(curFilename, "w")
        fpo.write(curGeoDataStr)
        fpo.close()
    except IOError:
        print "Failed to create file:" + curFilename
