// var apiKey = "YOUR KEY HERE";
var apiKey = "yVAps94148M2ZiXfJyUF";
/* global Plotly */
var url =
  `https://www.quandl.com/api/v3/datasets/WIKI/AMZN.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

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
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_date;
    var dates = unpack(data.dataset.data, 0);
    var closingPrices = unpack(data.dataset.data, 4);

    var selectorOptions = {
      buttons: [{
          step: 'month',
          stepmode: 'backward',
          // stepmode: 'todate',
          count: 1,
          label: '1m'
      }, {
          step: 'month',
          stepmode: 'backward',
          count: 6,
          label: '6m'
      }, {
          step: 'year',
          stepmode: 'todate',
          count: 1,
          label: 'YTD'
      }, {
          step: 'year',
          stepmode: 'backward',
          count: 1,
          label: '1y'
      }, {
          step: 'all',
      }],
    };

    var trace1 = {
      // type: "bar",
      // mode: "lines+markers",
      mode: "lines",
      name: name,
      x: dates,
      y: closingPrices,
      line: {
        color: "red"
      }
    };

    var data = [trace1];

    var layout = {
      title: `${stock} closing prices`,
      xaxis: {
        rangeselector: selectorOptions,
        rangeslider: {}
      },
      yaxis: {
        //Determina que el range sea zoomable
        //https://plotly.com/python/reference/layout/xaxis/
        fixedrange: true
        // rangemode: 'tozero'
      }
    };

    Plotly.newPlot("plot", data, layout);

  });
}

buildPlot();
