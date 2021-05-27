// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 660;

// Define the chart's margins as an object
var chartMargin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3.select("body")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Load data from hours-of-tv-watched.csv
// YOUR CODE HERE
d3.csv("hours-of-tv-watched.csv").then(function(tvData) {

  // console.log(tvData);

  // log a list of names
  var names = tvData.map(data => data.name);
  console.log("names", names);

  // Cast each hours value in tvData as a
  // number using the unary + operator
  tvData.forEach(function(data) {
    data.hours = +data.hours;
    console.log("Name:", data.name);
    console.log("Hours:", data.hours);
  });
});

  // Cast the hours value to a number for each piece of tvData


  // Configure a band scale for the horizontal axis with a padding of 0.1 (10%)


  // Create a linear scale for the vertical axis.


  // Create two new axes functions passing our scales in as arguments


  // Append two SVG group elements to the chartGroup area,
  // and create the bottom and left axes inside of them

  // Create one SVG rectangle per piece of tvData
  // Use the linear and band scales to position each rectangle within the chart
  // shift everything over by the margins

// scale y to chart height
var yScale = d3.scaleLinear()
.domain([0, d3.max(dataArray)])
.range([chartHeight, 0]);

// scale x to chart width
var xScale = d3.scaleBand()
.domain(dataCategories)
.range([0, chartWidth])
.padding(0.05);

// create axes
var yAxis = d3.axisLeft(yScale);
var xAxis = d3.axisBottom(xScale);

// set x to the bottom of the chart
chartGroup.append("g")
.attr("transform", `translate(0, ${chartHeight})`)
.call(xAxis);

// set y to the y axis
// This syntax allows us to call the axis function
// and pass in the selector without breaking the chaining
chartGroup.append("g")
.call(yAxis);

/* Note: The above code is equivalent to this:
  var g = chartGroup.append("g");

  yAxis(g);
*/
// Append Data to chartGroup
chartGroup.selectAll(".bar")
.data(dataArray)
.enter()
.append("rect")
.classed("bar", true)
.attr("x", (d, i) => xScale(dataCategories[i]))
.attr("y", d => yScale(d))
.attr("width", xScale.bandwidth())
.attr("height", d => chartHeight - yScale(d));
