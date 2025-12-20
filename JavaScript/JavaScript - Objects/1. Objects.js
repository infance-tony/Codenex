// Object literal
const obj1 = { key: "value" };

// Object constructor
const obj2 = new Object();
obj2.key = "value";

console.log(obj1);
console.log(obj2);

// Object operations

// Accessing properties
console.log(obj1.key); // Output: value

// Adding properties
obj1.newKey = "new value";
console.log(obj1); // Output: { key: "value", newKey: "new value" }

// Modifying properties
obj1.key = "updated value";
console.log(obj1.key); // Output: updated value

// Deleting properties
delete obj1.newKey;
console.log(obj1); // Output: { key: "updated value" }

// Checking if property exists
console.log("key" in obj1); // Output: true
console.log("nonexistent" in obj1); // Output: false

// Iterating over properties
for (let prop in obj1) {
    console.log(prop + ": " + obj1[prop]);
}
