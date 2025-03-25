// 1.
const birthYear = 2009;
console.log({ birthYear });

// 2.
let counter = 5;
counter-=2;
console.log({ counter });

// 3.
const E = Math.E;
console.log({ E });

// 4.
const divide = (a, b) => a / b;
console.log(divide(10, 2));

// 5.
const isEven = (num) => {
    if (num % 2 === 0) return true;
    return false;
}
console.log(isEven(5));

// 6.
const calculateVolume = (radius, height) => Math.PI * radius ** 2 * height;
console.log(calculateVolume(10, 20));

// 7.
const movie = {
    title: "Inception",
    year: 2010,
    director: "Christopher Nolan"
    };
const { title, year, director } = movie;
console.log({ year });
console.log({ director });

// 8.
const fruits = ["apple", "orange", "banana", "grape"];
const {first, second, third} = fruits;
console.log({ second });
console.log({ third });

// 9.
let make = window.prompt("Enter your car make: ");
let model = window.prompt("Enter your car model: ");
let carYear = window.prompt("Enter your car year: ");
console.log(`Your car is a ${make} ${model} made in ${carYear}`);