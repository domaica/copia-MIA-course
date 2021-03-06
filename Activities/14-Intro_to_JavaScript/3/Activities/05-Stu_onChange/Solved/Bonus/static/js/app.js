// grab references to the input element and the output div
var text = d3.select("#text");
var output = d3.select(".output");

function counter(text) {
  // convert text to lowercase characters (chars)
  var chars = text
    .toLowerCase()
    // elimina spaces entre caracteres
    .replace(/\s+/g, "")
    //hace split de la palabra en letras NO PARECE NECESARIO
    .split("");

  var counts = {};
  chars.forEach((char) => {
    if (char in counts) {
      counts[char] += 1;
    }
    else {
      counts[char] = 1;
    }
  });

  return counts;
}
// Function to handle input change
function handleChange(event) {
  // grab the value of the input field
  var value = d3.event.target.value;

  // clear the existing output
  output.html("");

  var frequencyCounts = counter(value);
  Object.entries(frequencyCounts).forEach(([key, value]) => {
    var li = output.append("li").text(`${key}: ${value}`);
  });

}
// PASSING A NAMED FUNCTION SEND 
// TO HANDLECHANGE SI CAMBIA EVENTO. presion Enter
text.on("change", handleChange);
