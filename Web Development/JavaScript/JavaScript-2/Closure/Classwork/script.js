// 4.
console.log("4.");
function printMessage(message) {
  return function () {
    console.log(message);
  };
}
printMessage("Hello, World!");
printMessage("I love JS!")();

// 5.
console.log("5.");
function calculateAverage() {
  let numbers = [1, 2, 3, 4, 5];
  return function (num) {
    numbers.push(num);
    let total = numbers.reduce((acc, curr) => acc + curr, 0);
    return total / numbers.length;
  };
}
calculateAverage();

// 6.
console.log("6.");
function createLogger() {
    return function (message) {
        const timestamp = new Date().toISOString();
        console.log(`[${timestamp}] ${message}`);
    };
}
const logger1 = createLogger();
const logger2 = createLogger();

logger1("This is the first log message.");
logger2("This is the second log message.");

// 7.
console.log("7.");
function createPasswordGenerator() {
    let length = prompt("Enter password length (default is 8):") || 8;
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    return function (newLength) {
        if (newLength) {
            length = newLength;
        }
        let password = '';
        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * characters.length);
            password += characters[randomIndex];
        }
        return password;
    };
}
const passwordGenerator = createPasswordGenerator();

// 8.
console.log("8.");
function calculateCircleArea(radius) {
    return function () {
        return Math.PI * radius * radius;
    };
}
calculateCircleArea(5)(); // Output: 78.53981633974483
calculateCircleArea(10)(); // Output: 314.1592653589793

// 9.
console.log("9.");
function createMultiplier(factor) {
    return function (number) {
        return number * factor;
    };
}

const multiplierBy2 = createMultiplier(2);
const multiplierBy5 = createMultiplier(5);

console.log(multiplierBy2(10));
console.log(multiplierBy2(3));
console.log(multiplierBy5(4));
console.log(multiplierBy5(7));

// 10.
console.log("10.");
function createToDoList() {
    let todos = [];

    return {
        addTodo: function (todo) {
            todos.push(todo);
            console.log(`Added todo: ${todo}`);
        },
        removeTodo: function (todo) {
            todos = todos.filter(t => t !== todo);
            console.log(`Removed todo: ${todo}`);
        },
        listTodos: function () {
            console.log("Current todos:", todos);
        }
    };
}
const myToDoList = createToDoList();
myToDoList.addTodo("Learn JavaScript");
myToDoList.addTodo("Practice coding");
myToDoList.listTodos();
myToDoList.removeTodo("Learn JavaScript");
myToDoList.listTodos();

// 11.
console.log("11.");
function createTimer() {
    let startTime = Date.now();
    return function () {
        let elapsedTime = Math.floor((Date.now() - startTime) / 1000);
        console.log(`Elapsed time: ${elapsedTime} seconds`);
    };
}

const timer1 = createTimer();
const timer2 = createTimer();

setTimeout(() => timer1(), 2000); 
setTimeout(() => timer2(), 3000); 
setTimeout(() => timer1(), 5000);