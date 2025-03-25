
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    sayHello() {
        console.log(`Hello, my name is ${this.name} and I am
    ${this.age} years old.`);
    }
}
const john = new Person('John', 25);
john.sayHello(); // Output: Hello, my name is John and I am 25 years old.

class Animal {
    constructor(name) {
        this.name = name;
    }
    makeSound() {
        console.log('Some generic sound');
    }
}

class Cat extends Animal {
    makeSound() {
       console.log(`${this.name} says Meow!`);
    }
}
const genericAnimal = new Animal('Mystery');
const myCat = new Cat('Whiskers');

console.log(myCat.name); // Output: Whiskers


class Dog extends Animal {
    makeSound() {
    super.makeSound(); // Calls the makeSound method of the
    superclass
        console.log('Bark Bark!');
    }
}