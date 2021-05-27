// An unsorted array
numArray = [9.9, 6.1, 17.1, 22.7, 4.6, 8.7, 7.2];

// Sort the array in descending order and assign the results to a variable
var sorted = numArray.sort(function sortFunction(a, b) {
  return a - b;
});

// Print the results to the console
console.log('Sorted: ',  sorted);

// Sort the array in descending order using an arrow function
// and assign the results to a variable and print to the console
var sortedByArrow = numArray.sort((a, b) => b - a);
console.log('Sorted con map arrow : ', sortedByArrow);

// Reverse the array order
var reversedArray = sortedByArrow.reverse();
console.log('Normal: ', numArray);
console.log('Reverse: ', reversedArray);

// Sort the array in ascending order using an arrow function
var sortedAscending = numArray.sort((a, b) => a - b);
console.log("Sort ascending: ", sortedAscending);

// Slice the first five elements of the sortedAscending array, assign to a variable
var sliced = sortedAscending.slice(0, 5);
console.log('Slice the first five element: ', sliced);
