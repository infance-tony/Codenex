// Public: Accessible from anywhere
class Example {
    constructor() {
        this.publicProperty = "This is public";
    }

    publicMethod() {
        console.log("Public method");
    }
}

// Private: Accessible only within the class (using #)
class ExamplePrivate {
    #privateProperty = "This is private";

    constructor() {
        this.#privateProperty = "Private value";
    }

    getPrivate() {
        return this.#privateProperty;
    }
}

// Protected: Not native in JS, but can be simulated with conventions or symbols
const protectedSymbol = Symbol('protected');

class ExampleProtected {
    constructor() {
        this[protectedSymbol] = "This is protected";
    }

    getProtected() {
        return this[protectedSymbol];
    }
}

// Usage
const pub = new Example();
console.log(pub.publicProperty); // Accessible
pub.publicMethod(); // Accessible

const priv = new ExamplePrivate();
// console.log(priv.#privateProperty); // Error: Private field
console.log(priv.getPrivate()); // Accessible via method

const prot = new ExampleProtected();
// console.log(prot[protectedSymbol]); // Conventionally not accessed directly
console.log(prot.getProtected()); // Accessible via method