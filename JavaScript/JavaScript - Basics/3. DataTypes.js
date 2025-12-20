// primitive data types
//1. Number: Represents numeric values (integers and decimals).
let n = 42;
let pi = 3.14;
//2. String: Represents text enclosed in single or double quotes.
let s = "Hello, World!";
//3. Boolean: Represents a logical value (true or false).
let bool= true;
//4. Undefined: A variable that has been declared but not assigned a value.
let notAssigned;
console.log(notAssigned);
Output
undefined
//5. Null: Represents an intentional absence of any value.
let empty = null;
//6. Symbol: Represents unique and immutable values, often used as object keys.
let sym = Symbol('unique');
//7. BigInt: Represents integers larger than Number.MAX_SAFE_INTEGER.
let bigNumber = 123456789012345678901234567890n;



// non-primitive data type
//1. Object: A collection of key-value pairs.
let person = {
    name: "Alice",
    age: 30
};

//2. Array: An ordered collection of values.
let numbers = [1, 2, 3, 4, 5];

//3. Function: A reusable block of code that performs a specific task.
function greet() {
    console.log("Hello!");
}
1
