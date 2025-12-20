function Animal(name) {
    this.name = name;
}
Animal.prototype.speak = function () {
    console.log(`${this.name} makes a sound.`);
};

// Child constructor function
function Dog(name) {
    Animal.call(this, name); // Inherit properties
}

// Inherit methods from Animal
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Adding a new method to Dog
Dog.prototype.bark = function () {
    console.log(`${this.name} barks: Woof!`);
};

// Creating an instance
const myDog = new Dog("Buddy");

myDog.speak(); 
myDog.bark();