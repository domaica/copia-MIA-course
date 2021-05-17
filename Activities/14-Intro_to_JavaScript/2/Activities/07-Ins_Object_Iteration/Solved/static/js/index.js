var userInfo = {
  name: "Eric",
  age: 32,
  location: "North America"
};

// Use `Object.values` and `forEach` to iterate through keys
console.log("object.keys y for each")
Object.keys(userInfo).forEach(key => console.log(key));
console.log("---------------------")


// Use `Object.values` and `forEach` to iterate through keys
console.log("object.values y for each")
Object.values(userInfo).forEach(value => console.log(value));
console.log("---------------------")

// Use `Object.entries` and `forEach` to iterate through keys and values
console.log("object.entries y for each")
Object.entries(userInfo).forEach(([key, value]) => 
console.log(`Key: ${key} and Value ${value}`));

console.log("---------------------")

// Array of objects
var users = [
  { name: "Eric", age: 32, location: "North America" },
  { name: "Sally", age: 23, location: "Europe" },
  { name: "Cassandra", age: 27, location: "North America" }];

// Loop through array of objects then each object


users.forEach((user) => {
  console.log(user);

  // Get the entries for each object in the array
  Object.entries(user).forEach(([key, value]) => {
    // Log the key and value
    console.log(`Key: ${key} and Value ${value}`);
  });
});
console.log("---------------------")
