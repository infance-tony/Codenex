// Example of an Object Constructor with different methods

// Constructor function
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// Adding methods to the prototype
Person.prototype.greet = function() {
    console.log('Hello, my name is ' + this.name);
};

Person.prototype.getAge = function() {
    return this.age;
};

Person.prototype.haveBirthday = function() {
    this.age++;
    console.log('Happy Birthday! Now ' + this.age + ' years old.');
};

// Creating an instance
var person1 = new Person('Alice', 30);

// Using the methods
person1.greet(); // Output: Hello, my name is Alice
console.log(person1.getAge()); // Output: 30
person1.haveBirthday(); // Output: Happy Birthday! Now 31 years old.
console.log(person1.getAge()); // Output: 31

