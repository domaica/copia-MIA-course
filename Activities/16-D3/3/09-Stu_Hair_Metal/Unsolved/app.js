var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("hairData.csv").then(function(hairData) {

    // Step 1: Parse Data/Cast as numbers
    // ==============================
    hairData.forEach(function(data) {
      // data.rockband = data.rockband;
      data.hair_length = +data.hair_length;
      data.num_hits = +data.num_hits;
    });

    // console.l
    // Step 2: Create scale functions
    // ==============================
    var xScale = d3.scaleLinear()
    .domain(d3.extent(hairData, d => d.hair_length))
    .range([0, width]);

  var yScale = d3.scaleLinear()
    .domain([0, d3.max(hairData, d => d.num_hits)])
    .range([height, 0]);

    // // // Step 3: Create axis functions
    // // // =============================
    // var xAxis = d3.axisBottom(xScale);
    // var yAxis = d3.axisLeft(yScale);
    // // // var yAxis = d3.axisLeft(yScale).ticks();

    // // // Step 4: Append Axes to the chart
    // // // ==============================
    // chartGroup.append("g")
    //   .attr("transform", `translate(0, ${height})`)
    //   .call(xAxis);

    // chartGroup.append("g")
    //   .call(yAxis);

      // Step 3: Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

      // line generator
      var line = d3.line()
        .x(d => xLinearScale(d.hair_length))
        .y(d => yLinearScale(d.num_hits));


    // Step 4: Append Axes to the chart
    // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    // Step 5: Create Circles
    // ==============================
    var circlesGroup = chartGroup.selectAll("circle")
    .data(hairData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.hair_length))
    .attr("cy", d => yLinearScale(d.num_hits))
    .attr("r", "15")
    .attr("fill", "pink")
    .attr("opacity", ".5");

    // Step 6: Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`${(d.rockband)}
      <br> Hair length: ${d.medals}
      <br> Hits: ${d.num_hits}`);
    });

    // Step 7: Create tooltip in the chart
    // ==============================
    chartGroup.call(toolTip);
    // Step 8: Create event listeners to display and hide the tooltip
    circlesGroup.on("mouseover", function(d) {
      toolTip.show(d, this);
    })
  // Método diferente con una función tip que tiene D3
    // Step 4: Create "mouseout" event listener to hide tooltip
      .on("mouseout", function(d) {
        toolTip.hide(d);
      });
  }).catch(function(error) {
    console.log(error);
  });
    
    // ==============================

    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Number of Billboard 100 Hits");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("Hair Metal Band Hair Length (inches)");

  // }).catch(function(error) {
  //   console.log(error);
  // });
