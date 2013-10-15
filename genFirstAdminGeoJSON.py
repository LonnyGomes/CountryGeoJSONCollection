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
adminNameKey=None
willForceUpdate=0
#shouldLint = 1
#validate_endpoint = 'http://geojsonlint.com/validate'

#if no  parameters are supplied, go with defaults
#otherwise parse the command line for the options
if len(sys.argv) > 1:
    #specify valid options
    shortOpts = "k:i:o:g:f"
    longOpts = [ "inputFile=", "outputPath=","keyName=","force", "genReadme="]

    try:
        opts, args = getopt.getopt(sys.argv[1:], shortOpts, longOpts)
        for opt,arg in opts:
            if opt in ("-k", "--keyName"):
                featureKey=arg
            elif opt in ("-i", "--inputFile"):
                inputFile=arg
            elif opt in ("-o", "--outputPath"):
                outputPath=arg
            elif opt in ("-g", "--genReadme"):
                adminNameKey=arg
            elif opt in ("-f", "--force"):
                willForceUpdate = 1

    except getopt.GetoptError as e:
        print """Invalid syntax!
        Usage: -k | --keyName <attribute key name in geojson file> 
               -i | --inputFile  <input geojson file> 
               -o | --outputPath <output path>
               -g | --genReadme <attribute key for country name in geojson file>
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
    sys.exit(-1)

print "Parsing ...",
sys.stdout.flush()
geoJSONData = json.loads(' '.join(geoJSONList))
print "DONE"

geoFeatures = geoJSONData["features"]


if adminNameKey:
    readmePath = outputPath + os.sep + "README.md"
    try:
        fpAdmin = open(readmePath, "w")
        fpAdmin.write("GeoJSON Countries list\n=====================\n")
    except IOError:
        print "Could not open %s for writing!" % readmePath
        adminNameKey = None

for curFeature in geoFeatures:
    curProperties = curFeature["properties"]
    curKey = curProperties[featureKey]
    
    print "Creating geojson file for " + curKey

    #if and admin key is defined, write out current country to readme file
    if adminNameKey:
        curAdminVal = curProperties[adminNameKey]
        if (curAdminVal):
            linkStr = u" - [{0}] (../../../blob/master/{1}/{2}.geojson)\n".format(curAdminVal, outputPath, curKey)
            fpAdmin.write(linkStr.encode("utf-8"))


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

if adminNameKey:
    fpAdmin.close()
