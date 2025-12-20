// Class definition
class Car {
  constructor(brand, model) {
    this.brand = brand; // property
    this.model = model; // property
  }

  // method
  showDetails() {
    console.log(`This car is a ${this.brand} ${this.model}.`);
  }
}

// Creating objects from the class
const car1 = new Car("Toyota", "Corolla");
const car2 = new Car("Honda", "Civic");

// Using the objects
car1.showDetails(); // This car is a Toyota Corolla.
car2.showDetails(); // This car is a Honda Civic.