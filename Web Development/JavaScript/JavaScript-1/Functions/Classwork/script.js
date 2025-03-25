// #1
function printMessage(){
    console.log("This is a function!");
}
printMessage();

// #2
function sayHello(name){
    console.log("Hello, " + name);
}
sayHello("Om");
sayHello("Ultimate Coders");

// #3
function calculateVolume(length, width, height){
    let volume = length * width * height;
    console.log(volume);
}
calculateVolume(3, 2, 5);

// #4
function computeAverage(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    let average = sum / numbers.length;
    console.log(average);
}
computeAverage([10, 20, 30, 40, 50]);

// #5
let globalCounter = 7;
function incrementCounter(){
    globalCounter++;
    console.log(globalCounter);
}
incrementCounter();
incrementCounter();
incrementCounter();

// #6
let externalVar = 42;
function accessOuterVar() {
    console.log(externalVar);
}
accessOuterVar();

// #7
function calculateBMI(weight, height){
    // weight:- kilograms
    // height:- meters
    let BMI = weight/(height*height);
    return BMI;
}
calculateBMI(70, 1.74);
calculateBMI(85, 1.73);
calculateBMI(90, 1.8542);

// #8
function findMax(num1, num2, num3){
    return Math.max([num1, num2, num3]);
}
findMax(5, 3, 9);
findMax(44, 33, 78);
findMax(7, 77, 777);

// #9
function orderFood(item, quantity = 1){
    console.log(`${item}:${quantity}`)
}
orderFood("Pizza", 3);
orderFood("Pizza");

// #10
function calculateFactorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * calculateFactorial(n - 1);
}

console.log(calculateFactorial(5)); // 120
console.log(calculateFactorial(7)); // 5040
console.log(calculateFactorial(10)); // 3628800

// #11
function isEven(number){
    if (number % 2 === 0){
        return true;
    }
    else{
        return false;
    }
}

console.log(isEven(7));
console.log(isEven(10));
console.log(isEven(18));
console.log(isEven(45));