var topojson = require('topojson');
var fs = require('fs');
var path = require('path');
var _ = require('underscore');

var geoJSONBasePath  = "geojson",
    topoJSONBasePath = "topojson";

var dataObj = {
    convertToTopo:function(geoPath, topoPath) {
        this.geoPath = geoPath;
        this.topoPath = topoPath;
        fs.readdir(geoPath, function (err, files){
            if (err) {
                console.log("Error reading path: " + err);
                return;
            }

            //process each file in folder for topoJSON
            _.each(files, dataObj.geoJSONIterator, dataObj);
        });
    },
    geoJSONIterator:function (element, index, list){
        //immediately return if not a geojson file
        if (path.extname(element) !== ".geojson") return;

        //load geojson file
        var file = this.geoPath + path.sep + element;
        var data = fs.readFileSync(file, {encoding: 'utf8'});

        console.log("Converting " + element + "...");
        var geoData = JSON.parse(data);
        var topoData = topojson.topology({collection: geoData});

        var topoFile = this.topoPath + path.sep + 
                       path.basename(element, ".geojson") +
                       ".topojson";

        //save out topojson file
        fs.writeFileSync(topoFile, 
                         JSON.stringify(topoData), 
                         {encoding: 'utf8'});
    }
};

dataObj.convertToTopo(geoJSONBasePath, topoJSONBasePath);
