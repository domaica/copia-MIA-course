// Dataset we will be using to set the height of our rectangles
var booksReadThisYear = [17, 23, 20, 34];

// Append an SVG wrapper to the page and set a variable equal to a reference to it
// YOUR CODE HERE

var svgHeight = 600;
var svgWidth = 400;

var svg = d3
  .select("#svg-area")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

//   var svgGroup = svg.append("g");

//   var y = d3.scale.linear()
//   .domain([minValue, maxValue])
//   .range([height, 0]);

// Vertical Bar Chart
// YOUR CODE HERE
svg.selectAll("rect")
  .data(booksReadThisYear)
  .enter()
  .append("rect")
  .classed('bar', true)
  
  .attr("width", 50)

  .attr("height", function(data) {
    return data * 10;
  })
  // Espacio en blanco entre barras son 50 de ancho y empieza en 60
  // por tanto les da 10 pixel de blanco
  .attr("x", function(data, index) {
    return index * 60;
  })
  .attr("y", function(data) {
    return 600 - data * 10;
  })
//   .attr("class", "bar");


// BONUS
// Horizontal Bar Chart
// YOUR CODE HERE

// BONUS 2
// Alter your Vertical bar chart code to go from bottom  up.
// Dataset we will be using to set the height of our rectangles.



