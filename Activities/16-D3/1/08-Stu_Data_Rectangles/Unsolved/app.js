// Data which we will be using to build our rectangle
var booksReadThisYear = [15];

// Append the SVG wrapper to the page, set its height and width, and create a variable which references it


// Append a rectangle and set its height in relation to the booksReadThisYear value
// Part 1
// Generating an SVG

var svg = d3.select("body").append("svg");

svg.attr("width", "600px").attr("height", "400px");

// Part 2
// Binding the SVG to data

var rectangles = svg.selectAll("rectangle");

var rValues = [40, 25, 10];

rectangles.data(rValues)
    .enter()
    .append("rectangle")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", 50) 
    
    function(d) {
      return d;
    })
    .attr("stroke", "black")
    .attr("stroke-width", "5")
    .attr("fill", "red");

    <rect x="0" y="0" width="50" height="50" fill="green" />