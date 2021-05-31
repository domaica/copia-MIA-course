// Selectable backgrounds of our map - tile layers:
// grayscale background.
var graymap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoiaWRvbWFpY2EiLCJhIjoiY2twMzJmaDh6MDFxbjJ2cXQyb2QyMzhwaiJ9.-FzfqNuduzuROgy0Sa423g");

// satellite background.
var satellitemap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoiaWRvbWFpY2EiLCJhIjoiY2twMzJmaDh6MDFxbjJ2cXQyb2QyMzhwaiJ9.-FzfqNuduzuROgy0Sa423g");

// outdoors background.
var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoiaWRvbWFpY2EiLCJhIjoiY2twMzJmaDh6MDFxbjJ2cXQyb2QyMzhwaiJ9.-FzfqNuduzuROgy0Sa423g");

// map object to an array of layers we created.
var map = L.map("mapid", {
  // USA center location
  center: [37.09, -95.71],
  zoom: 4,
  layers: [graymap, satellitemap, outdoors]
});

// adding one 'graymap' tile layer to the map.
graymap.addTo(map);

// layers for two different sets of data, earthquakes and tectonicplates.
var tectonicplates = new L.LayerGroup();
var earthquakes = new L.LayerGroup();

// base layers
var baseMaps = {
  "Satellite map": satellitemap,
  "Grayscale map": graymap,
  "Normal physical map": outdoors
};

// overlays 
var overlayMaps = {
  "Tectonic Plates": tectonicplates,
  "Earthquakes": earthquakes
};

// control which layers are visible.
L.control
  .layers(baseMaps, overlayMaps, {collapsed: true})
  .addTo(map);

// retrieve earthquake geoJSON data.
// d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson", function(data) {
  d3.json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson", function(data) {
    console.log(data.features);

  function styleInfo(feature) {
    return {
      // opacity: 1,
      fillOpacity: 0.8,
      fillColor: getColor(feature.geometry.coordinates[2]),
      // border
      color: "black",
      radius: getRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5
    };
  }

  // Define the color of the marker based on the magnitude of the earthquake.

  function getColor(depth) {
    switch (true) {
      case depth > 500:
        return "#42117D";
      case depth > 250:
        return "#720DBA";
      case depth > 100:
        return "#942FDC";
      case depth > 20:
        return "#D31BA4";
        // return "#EDE1F6";
      case depth > 10:
        return "#D64DB3";
        // return "#EDE1F6";
      default:
        return "#F99BE1";
        // return "#EDE1F6";
    }
  }

  // define the radius of the earthquake marker based on its magnitude.

  function getRadius(magnitude) {
    // if (magnitude === 0) {
    //   return 1;
    // }

    return magnitude * 3;
  }

  // add GeoJSON layer to the map
  L.geoJson(data, {
    pointToLayer: function(feature, latlng) {
      return L.circleMarker(latlng);
    },
    style: styleInfo,
    onEachFeature: function(feature, layer) {
      layer.bindPopup("<strong>Magnitude (Richter): </strong>" + feature.properties.mag 
      + "<br><strong>Location: </strong>" + feature.properties.place 
      // obtained 3rd coordinate
      + "<br><strong>Depth (km): </strong>" + feature.geometry.coordinates[2]);
    }

  }).addTo(earthquakes);

  earthquakes.addTo(map);


  var legend = L.control({
    position: "bottomleft"
  });


// 
legend.onAdd = function() {
  var div = L.DomUtil.create("div", "info legend");
  labels = ['<strong>Depth in Km.</strong>'];

  var grades = ['Elevation (depth < 0) ', 10, 20, 100, 250, 500];
  var colors = [
    "#F99BE1",
    "#D64DB3",
    "#D31BA4",
    // "#EDE1F6",
    // "#D9B9F2",
    // "#C092E5",
    "#942FDC",
    "#720DBA",
    "#42117D"
  ];
  labels.push('<title></title>');
  div.innerHTML = labels.join('<br>');

  for (var i = 0; i < grades.length; i++) {
    div.innerHTML += "<i style='background: " + colors[i] + "'></i> " +
      grades[i] + (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+");
  }
  return div;
};


legend.addTo(map);

  // retrive Tectonic Plate geoJSON data.
  d3.json("https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json",
    function(platedata) {
      console.log(platedata.features);

      L.geoJson(platedata, {
        color: "brown",
        dashArray: '4, 4', dashOffset: '0',
        opacity: "0.75",
        weight: 3
      })
      .addTo(tectonicplates);

      // add the tectonicplates layer to the map.
      tectonicplates.addTo(map);
    });
});