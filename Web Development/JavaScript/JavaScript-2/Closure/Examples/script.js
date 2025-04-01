// Example demonstrating Relationship with Lexical Scoping
function outerFunction() {
  let outerVariable = "I am from the outer function";
  function innerFunction() {
    console.log(outerVariable); // Accessing outerVariable from the outer scope
  }
  // Returning the inner function
  return innerFunction;
}
// Call outerFunction to get the inner function
let innerFunc = outerFunction();
// Even though outerFunction has finished executing,
// innerFunc still has access to outerVariable due to closure
innerFunc(); // Output: "I am from the outer function"

function greet(name) {
  return function () {
    console.log(`Hello, ${name}!`);
  };
}
let greetJohn = greet("John");
let greetEmily = greet("Emily");
greetJohn(); // Output: "Hello, John!"
greetEmily(); // Output: "Hello, Emily!"

function counter() {
  let count = 0;
  function increment() {
    count++;
    console.log(count);
  }
  increment();
}
counter(); // Output: 1

function createCounter() {
  let count = 0;
  return {
    increment: function () {
      count++;
      console.log(count);
    },
    decrement: function () {
      count--;
      console.log(count);
    },
  };
}
let myCounter = createCounter();
myCounter.increment(); // Output: 1
myCounter.increment(); // Output: 2

function handleClick() {
  let count = 0;
  return function () {
    count++;
    console.log(`Button clicked ${count} times`);
  };
}

let buttonClickHandler = handleClick();
document.getElementById("myButton").addEventListener("click", buttonClickHandler);

function add(x) {
  return function (y) {
    return x + y;
  };
}
let addFive = add(5);
console.log(addFive(3)); // Output: 8
console.log(addFive(7)); // Output: 12

function createClosure() {
  let bigData = "..."; // Large data
  // Function using bigData
  return function () {
    console.log(bigData);
  };
  // Explicitly nullify bigData reference
  bigData = null;
}

// Unnecessary closure
function processArray(arr) {
  arr.forEach(function (item) {
    // Processing logic
  });
}
// Avoiding unnecessary closure
function processArray(arr, callback) {
  arr.forEach(callback);
}

