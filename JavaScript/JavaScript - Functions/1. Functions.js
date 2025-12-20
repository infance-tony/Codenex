// Function Declaration: A function declared with the 'function' keyword. It can be called before its declaration due to hoisting.
function greet(name) {
    return `Hello, ${name}!`;
}

// Function Expression: A function assigned to a variable. It is not hoisted and must be defined before use.
const greet2 = function(name) {
    return `Hello, ${name}!`;
};

// Arrow Function: A concise syntax for function expressions, introduced in ES6. It does not have its own 'this' context.
const greet3 = (name) => `Hello, ${name}!`;

// Anonymous Function in setTimeout: An unnamed function passed as a callback to execute after a delay.
setTimeout(function() {
    console.log("Anonymous function executed");
}, 1000);

// IIFE (Immediately Invoked Function Expression): A function that runs immediately after its definition, often used to create a scope.
(function() {
    console.log("IIFE executed");
})();

// Constructor Function: A function that uses 'this' to set properties on an object created with 'new'.
function Person(name) {
    this.name = name;
    this.greet = function() {
        return `Hello, ${this.name}!`;
    };
}

// Calling functions
console.log(greet("World"));
console.log(greet2("JavaScript"));
console.log(greet3("Functions"));
console.log(new Person("Alice").greet());
