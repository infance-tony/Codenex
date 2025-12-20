// Simple JavaScript code demonstrating all array methods

let arr = [1, 2, 3, 4, 5];

// push: Adds elements to the end
arr.push(6); // [1, 2, 3, 4, 5, 6]

// pop: Removes the last element
arr.pop(); // [1, 2, 3, 4, 5]

// shift: Removes the first element
arr.shift(); // [2, 3, 4, 5]

// unshift: Adds elements to the beginning
arr.unshift(1); // [1, 2, 3, 4, 5]

// splice: Adds/removes elements at a specific index
arr.splice(2, 1, 10); // [1, 2, 10, 4, 5]

// slice: Returns a shallow copy of a portion
let sliced = arr.slice(1, 4); // [2, 10, 4]

// forEach: Executes a function for each element
arr.forEach(item => console.log(item)); // logs each item

// map: Creates a new array with results of calling a function
let mapped = arr.map(item => item * 2); // [2, 4, 20, 8, 10]

// filter: Creates a new array with elements that pass a test
let filtered = arr.filter(item => item > 3); // [10, 4, 5]

// reduce: Reduces the array to a single value
let reduced = arr.reduce((acc, item) => acc + item, 0); // 27

// find: Returns the first element that satisfies a condition
let found = arr.find(item => item > 4); // 10

// findIndex: Returns the index of the first element that satisfies a condition
let foundIndex = arr.findIndex(item => item > 4); // 2

// some: Tests if at least one element passes a test
let someResult = arr.some(item => item > 4); // true

// every: Tests if all elements pass a test
let everyResult = arr.every(item => item > 0); // true

// sort: Sorts the array
arr.sort((a, b) => a - b); // [1, 2, 4, 5, 10]

// reverse: Reverses the array
arr.reverse(); // [10, 5, 4, 2, 1]

// concat: Joins arrays
let newArr = arr.concat([6, 7]); // [10, 5, 4, 2, 1, 6, 7]

// join: Joins all elements into a string
let joined = arr.join('-'); // '10-5-4-2-1'

// indexOf: Returns the first index of an element
let index = arr.indexOf(4); // 2

// lastIndexOf: Returns the last index of an element
let lastIndex = arr.lastIndexOf(4); // 2

// includes: Checks if an array includes a certain value
let includesResult = arr.includes(5); // true

// flat: Flattens nested arrays
let nested = [1, [2, [3]]];
let flatArr = nested.flat(2); // [1, 2, 3]

// flatMap: Maps and flattens
let flatMapped = arr.flatMap(item => [item, item * 2]); // [10, 20, 5, 10, 4, 8, 2, 4, 1, 2]
