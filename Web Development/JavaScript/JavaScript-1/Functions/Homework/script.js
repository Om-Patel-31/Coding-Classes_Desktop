// #1
function greetUser() {
    console.log("Hello, user!");
}
greetUser();

// #2
function personalizedMessage(userName) {
    console.log(`Hello, ${userName}!`);
}
personalizedMessage("Alice");
personalizedMessage("Bob");

// #3
function calculateArea(base, height) {
    let area = 0.5 * base * height;
    return area;
}
console.log(calculateArea(5, 10));

// #4
function computeSum(numbers) {
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
}
console.log(computeSum([1, 2, 3, 4, 5]));

// #5
let totalClicks = 0;
function incrementClicks() {
    totalClicks++;
}
incrementClicks();
incrementClicks();
incrementClicks();
console.log(totalClicks);

// #6
let globalVar = "I am a global variable";
function displayGlobalVar() {
    console.log(globalVar);
}
displayGlobalVar(); // This will log "I am a global variable" because globalVar is accessible globally.

// #7
function convertTemperature(temperature, scale) {
    if (scale === "C") {
        return (temperature - 32) * 5 / 9;
    } else if (scale === "F") {
        return (temperature * 9 / 5) + 32;
    } else {
        return "Invalid scale";
    }
}
console.log(convertTemperature(100, "C"));
console.log(convertTemperature(0, "F"));

// #8
function findMin(num1, num2, num3) {
    return Math.min(num1, num2, num3);
}
console.log(findMin(3, 1, 2));
console.log(findMin(10, 5, 8));

// #9
function orderProduct(product, quantity = 1) {
    console.log(`Ordered ${quantity} of ${product}`);
}
orderProduct("Laptop");
orderProduct("Phone", 3);

// #10
function powerOfTwo(n) {
    return Math.pow(2, n);
}
console.log(powerOfTwo(3));
console.log(powerOfTwo(5));

// #11
function isPositive(number) {
    return number > 0;
}
console.log(isPositive(5));
console.log(isPositive(-3));
console.log(isPositive(0));