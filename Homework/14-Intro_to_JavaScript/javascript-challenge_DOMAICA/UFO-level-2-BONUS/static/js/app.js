// from data.js
var tableData = data;
// Viewing the available data from data.js
// console.log(tableData);


// Creating variables for table content and button
var tablecontent = d3.select("tbody");
var button = d3.select("#filter-btn");
// input fields creation so we can load content from data using d3.
var inputFieldDate = d3.select("#datetime");
var inputFieldCity = d3.select("#city");
var inputFieldState = d3.select("#state");
var inputFieldCountry = d3.select("#country");
var inputFieldShape = d3.select("#shape");
// Columns from data
var columns = ["datetime", "city", "state", "country", "shape", "durationMinutes", "comments"]
// console.log(columns);

// function to initial load / render of table
function init() {
    // Send table data to HTML to show populated table
    var addData = (dataInput) => {
        dataInput.forEach(ufoSightings => {
            var row = tablecontent.append("tr");
            columns.forEach(column => row.append("td").text(ufoSightings[column])
            )
        });
    }
    addData(tableData);
}

// function invoked to filter data and send content filtered to HTML
function filterdata(){

    // Creating an Event Listener for the Button
    // Setting up the Filter Button for Date and City
    button.on("click", () => {
        
        // Prevent page from refreshing
        d3.event.preventDefault();
        

        // Declare several variables to collect different input values introduced. 
        // Trim spaces from input and lowercase inputs to avoid errors doing comparisons with table content
        // https://www.w3schools.com/jsref/jsref_tolowercase.asp
        var inputDate = inputFieldDate.property("value").trim();
        // console.log(inputFieldDate)
        var inputCity = inputFieldCity.property("value").toLowerCase().trim();
        // console.log(inputFieldCity)
        var inputState = inputFieldState.property("value").toLowerCase().trim();
        // console.log(inputFieldState)
        var inputCountry = inputFieldCountry.property("value").toLowerCase().trim();
        // console.log(inputFieldCountry)
        var inputShape = inputFieldShape.property("value").toLowerCase().trim();
        // console.log(inputFieldShape)


        // Filtering table data in case one input is given (date, city, state, country or shape)
        var filterDate = tableData.filter(tableData => tableData.datetime === inputDate);
        console.log('date:', filterDate)
        var filterCity = tableData.filter(tableData => tableData.city === inputCity);
        console.log('city:',filterCity)
        var filterState = tableData.filter(tableData => tableData.state === inputState);
        console.log('state:',filterState)
        var filterCountry = tableData.filter(tableData => tableData.country === inputCountry);
        console.log('country:',filterCountry)
        var filterShape = tableData.filter(tableData => tableData.shape === inputShape);
        console.log('shape:',filterShape)

        
        // Filtering table data in case multiple categories are requested to filter (date, city, state, country or shape)
        // Combination date city
        var CombinedDateCity = tableData.filter(tableData => tableData.datetime === inputDate &&
            tableData.city === inputCity);
        console.log('date city:', CombinedDateCity)

        // Combination date state
        var CombinedDateState = tableData.filter(tableData => tableData.datetime === inputDate &&
            tableData.state === inputState);
        console.log('date state:', CombinedDateState)

        // Combination date country
        var CombinedDateCountry = tableData.filter(tableData => tableData.datetime === inputDate &&
            tableData.country === inputCountry);
        console.log('date country:', CombinedDateCountry)

        // Combination date shape
        var CombinedDateShape = tableData.filter(tableData => tableData.datetime === inputDate &&
            tableData.shape === inputShape);
        console.log('date shape:', CombinedDateShape)

        // Combination city shape
        var CombinedCityShape = tableData.filter(tableData => tableData.city === inputCity &&
            tableData.shape === inputShape);
        console.log('city shape:', CombinedCityShape)

        // Combination state shape
        var CombinedStateShape = tableData.filter(tableData => tableData.state === inputState &&
            tableData.shape === inputShape);
        console.log('state shape:', CombinedStateShape)
        
        // Combination country shape
        var CombinedCountryShape = tableData.filter(tableData => tableData.country === inputCountry &&
            tableData.shape === inputShape);
        console.log('country shape:', CombinedCountryShape)

        // Combination date city shape
        var CombinedDateCityShape = tableData.filter(tableData => tableData.datetime === inputDate &&
            tableData.city === inputCity &&
            tableData.shape === inputShape);
        console.log('date city shape:', CombinedDateCityShape)

        // Combination date state shape
        var CombinedDateStateShape = tableData.filter(tableData => tableData.datetime === inputDate &&
            tableData.state === inputState &&
            tableData.shape === inputShape);
        console.log('date state shape:', CombinedDateStateShape);

        // Combination city state shape
        var CombinedCityStateShape = tableData.filter(tableData => tableData.city === inputCity &&
            tableData.state === inputState &&
            tableData.shape === inputShape);
        console.log('city state shape:', CombinedCityStateShape);
        
        
        //Empty table to get new filtered content
        tablecontent.html("");

        // function to add filtered data to HTML table
        var addDatafiltered = (filterDate) => {
            filterDate.forEach(ufosight => {
                var row = tablecontent.append("tr");
                columns.forEach(column => row.append("td").text(ufosight[column])
                )
            });
        }


        // Send data to HTML according to filtered content.
        if(CombinedDateStateShape.length !== 0) {
            addDatafiltered(CombinedDateStateShape);
            }
        else if(CombinedCityStateShape.length !== 0){
                addDatafiltered(CombinedCityStateShape);
                }
        else if(CombinedDateCityShape.length !== 0){
            addDatafiltered(CombinedDateCityShape);
            }
        else if(CombinedCountryShape.length !== 0){
            addDatafiltered(CombinedCountryShape);
            }
        else if(CombinedStateShape.length !== 0){
            addDatafiltered(CombinedStateShape);
            }
        else if(CombinedCityShape.length !== 0){
            addDatafiltered(CombinedCityShape);
            }
        else if(CombinedDateShape.length !== 0){
            addDatafiltered(CombinedDateShape);
            }
        else if(CombinedDateCountry.length !== 0){
            addDatafiltered(CombinedDateCountry);
            }
        else if(CombinedDateState.length !== 0){
            addDatafiltered(CombinedDateState);
            }
        else if(CombinedDateCity.length !== 0){
            addDatafiltered(CombinedDateCity);
            }
        else if(filterDate.length !== 0){
            addDatafiltered(filterDate);
            }
        else if(filterCity.length !== 0){
            addDatafiltered(filterCity);
            }
        else if(filterState.length !== 0){
            addDatafiltered(filterState);
            }
        else if(filterCountry.length !== 0){
            addDatafiltered(filterCountry);
            }
        else if(filterShape.length !== 0){
            addDatafiltered(filterShape);
            }
        // In case of no data filtered or input error check. Message in the table as rows
        else {
                tablecontent.append("tr").append("td").text("NO DATA.");
                tablecontent.append("tr").append("td").text("There are 2 possible reasons you are here:");
                tablecontent.append("tr").append("td").text("1. Please check your input format.");
                tablecontent.append("tr").append("td").text("2. There is no data for your data filter combination");
            }
    })
}
// Invoke function to filter table data
filterdata();
// Render initial table load
init();

