// Sort the data by Greek search results
var sortedByGreekSearch = data.sort((a, b) => b.greekSearchResults - a.greekSearchResults);
console.log(sortedByGreekSearch);

// Slice the first 10 objects for plotting
var slicedData = sortedByGreekSearch.slice(0, 10);
console.log(slicedData);

//EXPERIMENT
var intento = slicedData.reverse();
var intento10 = intento.slice(0, 10);
console.log('Test reverse:',intento10);

// Reverse the array to accommodate Plotly's defaults
var reversedData = slicedData.reverse();
console.log(reversedData);

// Trace1 for the Greek Data
var trace1 = {
  x: reversedData.map(object => object.greekSearchResults),
  y: reversedData.map(object => object.greekName),
  text: reversedData.map(object => object.greekName),
  name: "Greek",
  type: "bar",
  orientation: "h"
};

// data
var data = [trace1];

// Apply the group bar mode to the layout
var layout = {
  title: "Greek gods search results",
  margin: {
    l: 100,
    r: 100,
    t: 100,
    b: 100
  }
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
