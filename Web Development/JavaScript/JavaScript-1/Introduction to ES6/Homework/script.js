// #1
let currentTemperature = -14;
console.log(currentTemperature);

// #2
const pi = 3.14;
console.log(pi);
// pi = 5; TypeError: Assignment to constant variable.

// #3
const calculateArea = (length, width) => length*width;
console.log(calculateArea);

// #4
let friendName = "Ben";
let greetingMessage = `Hey ${friendName}!`;
console.log(greetingMessage);

// #5
let day = "Wednesday";
let month = "January";
let year = 2025;
let dateMessage = `Today is ${day} of ${month}, ${year}`;
console.log(dateMessage);

// #6
let flowers = ["rose", "tulip", "daisy"];
let [firstFlower, , lastFlower] = flowers;
console.log(firstFlower, lastFlower);

// #7
let sizes = ["small", "medium", "large", "extra-large"];
let [firstSize, ...remainingSizes] = sizes;
console.log(remainingSizes.length);

// #8
let car = { make: "Toyota", model: "Corolla", newYear: 2020 };
let { make, model, newYear } = car;
console.log(make, model, year);

// #9
let friendDetails = { newFriendName: "John" };
let { newFriendName = "Jane" } = friendDetails;
console.log(friendName);