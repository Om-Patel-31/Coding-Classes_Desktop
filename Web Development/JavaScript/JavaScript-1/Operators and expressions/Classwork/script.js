// #4
let tempCelsius = 0;
let tempFahrenheit = (tempCelsius * 9/5) + 32;
console.log(tempFahrenheit);

// #5
let cartAmount = 120;
let discount = 0.2 * cartAmount;
let totalAmount = cartAmount - discount;
console.log(totalAmount);

// #6
let userAge = parseInt(alert("Enter your age:"));
let hasDriverLicense = alert("Do you have a valid driver's license?(true/false)") === "true";

let isEligibleToRent = userAge >= 18 && hasDriverLicense;
console.log("Eligible to rent a car:", isEligibleToRent);

// #7
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName;
console.log("Full name:", fullName);

// #8
let year = 2024;
let isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
console.log("Is leap year:", isLeapYear);

// #9
let number = 3;
let square = number ** 2;
let cube = number ** 3;
console.log("Square:", square, "Cube:", cube);

// #10
let userInput = "5";
let result = Number(userInput) + 10;
console.log("Result:", result);

// #11
let inventory = 50;
inventory -= 10;
console.log("Updated inventory:", inventory);

// #12
let userGuess = 3;
let randomNumber = Math.floor(Math.random() * 5) + 1;
let guessedCorrectly = userGuess === randomNumber;
console.log("Guessed correctly:", guessedCorrectly);

// #13
let preferredModeOfTransportation = "car";
let isPreferred = preferredModeOfTransportation === "car" || preferredModeOfTransportation === "bike";
console.log("Preferred mode of transportation:", isPreferred ? "Car or Bike" : "Other");