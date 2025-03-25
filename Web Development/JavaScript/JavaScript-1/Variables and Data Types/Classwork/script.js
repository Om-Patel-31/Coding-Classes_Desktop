let currentTemperature = -2;
console.log(currentTemperature);

let favoriteColor = "blue";
favoriteColor = "green";
console.log(favoriteColor);

{
    let x = 5;
    console.log(x);
}

const PI = 3.14;
let circleRadius = 10;
let area = PI * circleRadius * circleRadius;
console.log(area);

let myVar = "Hello";
let myvar = "World";
console.log(myVar);
console.log(myvar);

let firstName = "John";
let lastName = "Doe";
let userAge = 30;
console.log(firstName, lastName, userAge);

let temperature = -2;
console.log(typeof temperature);
let weatherStatus = "Snowy";
console.log(typeof weatherStatus);

let car = {
    brand: "Koenigsegg",
    model: "Gemera",
    year: 2022,
    startEngine: function() {
        console.log("Engine started");
    }
};
console.log(car.brand);
console.log(car.model);
console.log(car.year);
car.startEngine();

console.log("5" == 5);
console.log("5" === 5);

let str = "true";
let boolValue = Boolean(str);
console.log(boolValue);