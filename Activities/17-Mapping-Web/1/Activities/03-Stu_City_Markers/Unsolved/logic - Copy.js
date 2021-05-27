// Create a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// City markers

// Add code to create a marker for each city below and add it to the map

// newyork;
var marker = L.marker([40.71, -74.00], {
  draggable: true,
  title: "New York"
}).addTo(myMap);

// chicago;
var marker = L.marker([45.52, -87.62], {
  draggable: true,
  title: "New York"
}).addTo(myMap);
// houston;
var marker = L.marker([29.76, -95.36], {
  draggable: true,
  title: "houston"
}).addTo(myMap);
// la;
var marker = L.marker([34.05, -118.24], {
  draggable: true,
  title: "Los Angeles"
}).addTo(myMap);
// omaha;
var marker = L.marker([41.20, -95.96], {
  draggable: true,
  title: "Omaha"
}).addTo(myMap);


