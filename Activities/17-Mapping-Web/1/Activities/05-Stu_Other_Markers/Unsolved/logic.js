// Create our initial map object
// Set the longitude, latitude, and the starting zoom level
var myMap = L.map("map").setView([39.8283, -98.5795], 5);

// Add a tile layer (the background map image) to our map
// Use the addTo method to add objects to our map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: "pk.eyJ1IjoiaWRvbWFpY2EiLCJhIjoiY2twMzJmaDh6MDFxbjJ2cXQyb2QyMzhwaiJ9.-FzfqNuduzuROgy0Sa423g"
}).addTo(myMap);

// Create a red circle over Dallas

L.marker([32.77, -96.79]).addTo(myMap);

L.circle([32.77, -96.79], {
  color: "red",
  fillColor: "red",
  fillOpacity: 0.25,
  radius: 100000
}).addTo(myMap);

// Connect a black line from NYC to Toronto

L.marker([40.71, -74.00]).addTo(myMap);

L.marker([43.65, -79.38]).addTo(myMap);
var line = [
  [40.71, -74.00],
  [43.65, -79.38]
];

L.polyline(line, {
  color: "black"
}).addTo(myMap);


// Create a purple polygon that covers the area in Atlanta, Savannah, Jacksonville and Montgomery

L.marker([33.74, -84.38]).addTo(myMap);

L.marker([32.08, -81.09]).addTo(myMap);

L.marker([30.33, -81.65]).addTo(myMap);

L.marker([32.37, -86.30]).addTo(myMap);

L.polygon([
  [33.74, -84.38],
  [32.08, -81.09],
  [30.33, -81.65],
  [32.37, -86.30]
], {
  color: "yellow",
  fillColor: "yellow",
  fillOpacity: 0.75
}).addTo(myMap);