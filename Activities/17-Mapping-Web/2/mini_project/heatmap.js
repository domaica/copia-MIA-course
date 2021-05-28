var myMap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 13
});
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: "pk.eyJ1IjoiaWRvbWFpY2EiLCJhIjoiY2twMzJmaDh6MDFxbjJ2cXQyb2QyMzhwaiJ9.-FzfqNuduzuROgy0Sa423g"
}).addTo(myMap);


var file = "pizza.csv";
d3.csv(file, function(response) {
  console.log(response);
  var heatArray = [];
  for (var i = 0; i < response.length; i++) {
    var location = response[i].location;
    if (location) {
      heatArray.push([location.coordinates[1], location.coordinates[0]]);
    }
  }
  var heat = L.heatLayer(heatArray, {
    radius: 20,
    blur: 35
  }).addTo(myMap);
});