// Array of movie ratings
var movieScores = [
  4.4,
  3.3,
  5.9,
  8.8,
  1.2,
  5.2,
  7.4,
  7.5,
  7.2,
  9.7,
  4.2,
  6.9
];

// Starting a rating count
var sum = 0;

// Arrays to hold movie scores
var goodMovies = [];
var okMovies = [];
var badMovies = [];

for (var i = 0; i < movieScores.length; i++) {

  var score = movieScores[i];
  sum += score;

  if (score > 7) {
    goodMovies.push(score);
  }
  else if (score <= 7 && score > 5) {
    okMovies.push(score);
  }
   else {
    badMovies.push(score);
  }
}

var numGoodMovies = goodMovies.length;
var numOkMovies = okMovies.length;
var numBadMovies = badMovies.length;

var avg = sum / movieScores.length;


// Print results
console.log("---------");
console.log(`There are ${numGoodMovies} good movies.`);
console.log(`There are ${numOkMovies} ok movies.`);
console.log(`There are ${numBadMovies} bad movies.`);
console.log("---------");
console.log(" ");
console.log(`The average movie rating is ${avg}.`);
console.log("---------");


