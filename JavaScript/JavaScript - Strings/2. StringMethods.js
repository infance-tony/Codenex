// String Methods in JavaScript

let str = "Hello, World!";

// Length of the string
console.log(str.length); // 13

// Convert to uppercase
console.log(str.toUpperCase()); // "HELLO, WORLD!"

// Convert to lowercase
console.log(str.toLowerCase()); // "hello, world!"

// Get character at index
console.log(str.charAt(0)); // "H"

// Find index of substring
console.log(str.indexOf("World")); // 7

// Extract substring
console.log(str.substring(7, 12)); // "World"

// Slice the string
console.log(str.slice(7, 12)); // "World"

// Replace substring
console.log(str.replace("World", "JavaScript")); // "Hello, JavaScript!"

// Split into array
console.log(str.split(", ")); // ["Hello", "World!"]

// Trim whitespace
let str2 = "  Hello  ";
console.log(str2.trim()); // "Hello"

// Check if starts with
console.log(str.startsWith("Hello")); // true

// Check if ends with
console.log(str.endsWith("!")); // true

// Includes substring
console.log(str.includes("World")); // true

