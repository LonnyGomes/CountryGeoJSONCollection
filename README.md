Country GeoJSON Collection
==========================

This is a collection of GeoJSON files of all first admin boundaries generated from the natural earth dataset.
Currently only small scale geojson files are generated, the hope is to support larger scale representations.
Feel free to use these files in your GIS projects.

Prerequisites
-------------
To regenerate the geojson files, ogr2ogr is used which is part of GDAL and can be downloaded [here](http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries).
In addition to GDAL, python and bash are needed as well. You get all this for free on a UNIX based system.

Usage
-----
To make changes to the geojson files, replace the countries.shp and companying files wit your dataset.
Then you must run the *convertShp2JSON* shell script that will generate a countries.geojson file.

Next you must run the *genFirstAdminGeoJSON* python script. If run without arguments, the countries.geojson file will be read and everything is outputed into the geojson folder.
The python script does support command line options for customization purposes

    ./genFirstAdminGeoJSON.py [ -k <key_name> | --keyName <key_name> ] | 
                              [ -i <input_file> | --inputFile <input_file> ] |
                              [ -o <output_path> | --outputPath <output_path> ] |
                              [ -f | --force ]
                              
               -k <arg>, --keyName <arg>     specify the attribute in the geojson properties object to use as primary key
                                             this should be a unique identifier, preferably the country code
               -i <arg> , --inputFile <arg>  specify the source geojson file to read in
                                             this file should be a feature collection of first admin geometries deprojected to WGS84
               -o <arg>, --outputPath <arg>  specify the output directory all geojson files should be created in
               -f , --force if supplied, existing files will be overwritten
