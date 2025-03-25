// 1. Define a class Car
class Car {
    constructor(make, year) {
        this.make = make;
        this.year = year;
    }
    startEngine() {
        console.log(`${this.make} (${this.year}) engine started.`);
    }
}

// 2. Instantiate two Car objects
const car1 = new Car('Toyota', 2022);
const car2 = new Car('Honda', 2021);
car1.startEngine();
car2.startEngine();

// 3. Define a class Employee
class Employee {
    constructor(name, position) {
        this.name = name;
        this.position = position;
    }
    introduce() {
        console.log(`Hello, my name is ${this.name} and I am a ${this.position}.`);
    }
}

// 4. Instantiate an Employee object
const emp1 = new Employee('Alice', 'Manager');
emp1.introduce();

// 5. Define a class Animal
class Animal {
    constructor(species) {
        this.species = species;
    }
}

// 6. Define a subclass Bird extending Animal
class Bird extends Animal {
    constructor(species, wingspan) {
        super(species);
        this.wingspan = wingspan;
    }
}

// 7. Instantiate objects from Animal and Bird classes
const animal = new Animal('Lion');
const bird = new Bird('Eagle', '2m');
console.log(`Animal species: ${animal.species}`);
console.log(`Bird species: ${bird.species}, Wingspan: ${bird.wingspan}`);

// 8. Define a class Movie
class Movie {
    constructor(title, genre) {
        this.title = title;
        this.genre = genre;
    }
    playMovie() {
        console.log(`Now playing: ${this.title} (${this.genre})`);
    }
}

// 9. Define a subclass Documentary extending Movie
class Documentary extends Movie {
    constructor(title, genre, subject) {
        super(title, genre);
        this.subject = subject;
    }
}

// 10. Instantiate objects from Movie and Documentary classes
const movie = new Movie('Inception', 'Sci-Fi');
movie.playMovie();

const doc = new Documentary('Planet Earth', 'Nature', 'Wildlife');
console.log(`Documentary Subject: ${doc.subject}`);