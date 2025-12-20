// Method Overloading Simulation in JavaScript
// JavaScript doesn't support method overloading natively, but we can simulate it using arguments.length or rest parameters.

class Calculator {
    add(...args) {
        if (args.length === 2) {
            return args[0] + args[1];
        } else if (args.length === 3) {
            return args[0] + args[1] + args[2];
        } else {
            return args.reduce((sum, num) => sum + num, 0);
        }
    }
}

// Method Overriding in JavaScript
class Animal {
    speak() {
        console.log("Animal makes a sound");
    }
}

class Dog extends Animal {
    speak() {
        console.log("Dog barks");
    }
}

class Cat extends Animal {
    speak() {
        console.log("Cat meows");
    }
}

// Usage
const calc = new Calculator();
console.log(calc.add(1, 2)); // 3
console.log(calc.add(1, 2, 3)); // 6

const dog = new Dog();
const cat = new Cat();
dog.speak(); // Dog barks
cat.speak(); // Cat meows