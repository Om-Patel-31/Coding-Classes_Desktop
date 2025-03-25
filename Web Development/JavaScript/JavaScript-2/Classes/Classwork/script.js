// 1.
class Product{
    constructor(name, price){
        this.name = name;
        this.price = price;
    }
    displayInfo(){
        console.log(`Product: ${this.name}, Price: ${this.price}`);
    }
}
let product1 = new Product('Milk', 1.5);
product1.displayInfo();

// 2.
let product2 = new Product('Bread', 2.0);
let product3 = new Product('Cheese', 3.5);
product2.displayInfo();
product3.displayInfo();

// 3.
class Customer {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    makePurchase() {
        console.log(`${this.name} made a purchase.`);
    }
}

// 4.
class Shape {
    constructor(color) {
        this.color = color;
    }
}

// 5.
class Circle extends Shape {
    constructor(color, radius) {
        super(color);
        this.radius = radius;
    }
}
let shape1 = new Shape('Red');
let circle1 = new Circle('Blue', 5);
console.log(`Shape color: ${shape1.color}`);
console.log(`Circle color: ${circle1.color}, Radius: ${circle1.radius}`);

// 6.
class Library{
    constructor(name, location){
        this.name = name;
        this.location = location;
    }
    openLibrary(){
        console.log(`${this.name} is now open at ${this.location}.`);
    }
}

// 7.
class Bookshelf {
    constructor(shelves){
        this.shelves = shelves;
    }
}
let library1 = new Library('Central Library', 'Downtown');
library1.openLibrary();

let bookshelf1 = new Bookshelf(5);
console.log(`Number of shelves: ${bookshelf1.shelves}`);