// Constructor methods in JavaScript are special methods in classes that are automatically called when an object is created using the 'new' keyword.
// They are used to initialize the object's properties and set up the initial state of the object.

// Example of a constructor method in a class:

class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  // Method to display person details
  display() {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
  }
}

// Creating an instance using the constructor
const person1 = new Person('Alice', 30);
person1.display(); // Output: Name: Alice, Age: 30