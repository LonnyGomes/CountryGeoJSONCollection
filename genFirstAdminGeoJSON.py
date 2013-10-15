#!/usr/bin/python
import requests
import json
import os
import sys
import getopt
import string

featureKey="ne_10m_adm"
inputFile="countries.geojson"
outputPath = "geojson"
willForceUpdate=0
#shouldLint = 1
#validate_endpoint = 'http://geojsonlint.com/validate'

#if no  parameters are supplied, go with defaults
#otherwise parse the command line for the options
if len(sys.argv) > 1:
    #specify valid options
    shortOpts = "k:i:of"
    longOpts = [ "inputFile=", "outputPath=","keyName=","force"]

    try:
        opts, args = getopt.getopt(sys.argv[1:], shortOpts, longOpts)
        for opt,arg in opts:
            if opt in ("-k", "--keyName"):
                featureKey=arg
            elif opt in ("-i", "--inputFile"):
                inputFile=arg
            elif opt in ("-o", "--outputPath"):
                outputPath=arg
            elif opt in ("-f", "--force"):
                willForceUpdate = 1

    except getopt.GetoptError as e:
        print """Invalid syntax!
        Usage: -k | --keyName <attribute key name in shape file> 
               -i | --inputFile  <input geojson file> 
               -o | --outputPath <output path>
               -f if supplied, existing files will be overwritten
        """
        sys.exit(-1)

try:
    print "Reading geojson file: %s ..." % inputFile,
    sys.stdout.flush()

    fp = open(inputFile)
    geoJSONList = fp.readlines()
    fp.close
    print "DONE"
except IOError:
    print "Could not open geojson file for reading:" + inputFile
    exit(-1)

print "Parsing ...",
sys.stdout.flush()
geoJSONData = json.loads(' '.join(geoJSONList))
print "DONE"

geoFeatures = geoJSONData["features"]

for curFeature in geoFeatures:
    curProperties = curFeature["properties"]
    curKey = curProperties[featureKey]

    print "Creating geojson file for " + curKey

    curFilename = outputPath + os.sep +  curKey + ".geojson"

    if os.path.exists(curFilename):
        if willForceUpdate:
            os.remove(curFilename)
        else:
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
