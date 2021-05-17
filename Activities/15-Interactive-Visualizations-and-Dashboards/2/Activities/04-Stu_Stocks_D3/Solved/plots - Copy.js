// var apiKey = "YOUR KEY HERE";
var apiKey = "   ";

/* global Plotly */
// ENMEDIO DE AQUI PONES EL DATASET_CODE QUE ES EL TICKER
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/TSLA.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Close
 * index 5 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

function buildPlot() {
  // then means return the data
  d3.json(url).then(function(data) {

    // Grab values from the data json object to build the plots
    var name = data.dataset.name;
    // Ticker de la accion dataset_code se pasa a var stock para luego
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_date;
    // Llama al index 0 que es Dates
    var dates = unpack(data.dataset.data, 0);
        // Llama al index 0 que es Closing price
    var closingPrices = unpack(data.dataset.data, 4);

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: dates,
      y: closingPrices,
      line: {
        color: "turquoise"
      }
    };

    var data = [trace1];

    var layout = {
      //Titulo con el ticker symbol del stock recogido de dataset_code antes
      title: `${stock} closing prices`,
      xaxis: {
        // EXPERIMENTO
        range: [startDate, '2018-03-27'],
        // range: [startDate, endDate],
        // autorange: true,
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("plot", data, layout);

  });
}

buildPlot();
