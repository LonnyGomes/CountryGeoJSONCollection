Country GeoJSON Collection
==========================

This is a collection of GeoJSON files of all country boundaries generated from the natural earth dataset.
The data is derived from the [Natural Earth 1:10m cultural vectors](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/).
Feel free to use these files in your GIS projects.

Prerequisites
-------------
To regenerate the geojson files, ogr2ogr is used which is part of GDAL and can be downloaded [here](http://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries).
In addition to GDAL, python and bash are needed as well. You get all this for free on a UNIX based system.

Usage
-----
To make changes to the geojson files, replace the countries.shp and accompanying files with your dataset.
Run the `convertShp2JSON` shell script to generate a countries.geojson file.

The `genCountriesGeoJSON` python script extracts the countries out of the `countries.geojson` file. If run without arguments, the countries.geojson file will be read and everything is outputted into the geojson folder.
The python script supports command line options for customization purposes

    ./genCountriesGeoJSON.py  [ -k <key_name> | --keyName <key_name> ] |
                              [ -i <input_file> | --inputFile <input_file> ] |
                              [ -o <output_path> | --outputPath <output_path> ] |
                              [ -g <admin_key_name> | --genReadme <admin_key_name> ] |
                              [ -f | --force ]

               -k <arg>, --keyName <arg>     specify the attribute in the geojson properties object
                                             to use as primary key
                                             this should be a unique identifier, preferably the country
                                             code or another identifying value

               -i <arg> , --inputFile <arg>  specify the source geojson file to read in
                                             this file should be a feature collection of country
                                             geometries deprojected to WGS84

               -o <arg>, --outputPath <arg>  specify the output directory all geojson files should be
                                             created in

               -g <arg>, --genReadme <arg>   specify the attribute in the geojson properties object that
                                             contains the official name of the country.
                                             The value is expected to be encoded in UTF-8

               -f , --force                  if supplied, existing files will be overwritten

To generate the topojson files, you must have node installed and run the following commands:

```
$ npm install
$ npm start
```

Examples
--------

The following example uses the python script given the following parameters
- the primary key property in the GeoJSON is "country_code"
- input file is names boundaries.geojson
- the output folder is geo_data
- a README.md is generated with the GeoJSON file with the admin name key being "country_name"

    ./genCountriesGeoJSON.py -k country_code -i boundaries.geojson -o geo_data -g country_name

The resulting geojson files should be stored in the geo_data folder (which must exist beforehand) with a README.md file that is also generated in the same folder.

Upcoming features
-----------------
I plan to use the GDAL python bindings to handle the conversion of the shapefile rather than relying on the external shell script.
