//artimatic operators
const sum = 5 + 3; // Addition
const diff = 10 - 2; // Subtraction
const p = 4 * 2; // Multiplication
const q = 8 / 2; // Division
console.log(sum, diff, p, q);

//assignment operators
let n = 10;
n += 5;
n *= 2;
console.log(n);

//comparison operators
console.log(10 > 5);
console.log(10 === "10");

//logical operators
const a = true;
const b = false;
console.log(a && b);
console.log(a || b);
console.log(!a);            

//ternary operator
const age = 18;
const canVote = (age >= 18) ? "Yes" : "No";
console.log(canVote);

//typeof operator
console.log(typeof sum);
console.log(typeof canVote);

//delete operator
const obj = { name: "Alice", age: 25 };
delete obj.age;
console.log(obj);

//instanceof operator
const date = new Date();
console.log(date instanceof Date);

//spread operator
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2);

//comma operator
let x = (1, 2, 3);
console.log(x); // Outputs 3

//string operators
const str1 = "Hello, ";
const str2 = "World!";
const greeting = str1 + str2;
console.log(greeting);

//chaining operators
const result = (5 + 3) * 2 > 10 ? "Greater" : "Lesser";
console.log(result);

