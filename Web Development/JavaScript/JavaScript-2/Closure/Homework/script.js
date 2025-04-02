// 1
function createFullName(firstName, lastName) {
    return function() {
        return `${firstName} ${lastName}`;
    };
}
const fullName1 = createFullName("John", "Doe");
const fullName2 = createFullName("Jane", "Smith");
console.log(fullName1());
console.log(fullName2());

// 2
function calculateRunningTotal() {
    let total = 0;
    return function(number) {
        total += number;
        return total;
    };
}
const runningTotal1 = calculateRunningTotal();
console.log(runningTotal1(5)); // Output: 5
console.log(runningTotal1(10)); // Output: 15

const runningTotal2 = calculateRunningTotal();
console.log(runningTotal2(3)); // Output: 3
console.log(runningTotal2(7)); // Output: 10

// 3
function createCounterLogger() {
    let count = 0;
    return function() {
        count++;
        console.log(`Count: ${count}, Timestamp: ${new Date().toISOString()}`);
    };
}

const counter1 = createCounterLogger();
counter1();
counter1();

const counter2 = createCounterLogger();
counter2();

// 4
function createRandomNumberGenerator(min, max) {
    return function() {
        return Math.random() * (max - min) + min;
    };
}

const randomGen1 = createRandomNumberGenerator(1, 10);
console.log(randomGen1());

const randomGen2 = createRandomNumberGenerator(20, 30);
console.log(randomGen2());

// 5
function calculateRectangleArea() {
    return function(width, height) {
        return width * height;
    };
}

const rectangleArea = calculateRectangleArea();
console.log(rectangleArea(5, 10)); // Output: 50
console.log(rectangleArea(7, 3)); // Output: 21

// 6
function createDivider(divisor) {
    return function(number) {
        return number / divisor;
    };
}

const divider1 = createDivider(2);
console.log(divider1(10)); // Output: 5

const divider2 = createDivider(5);
console.log(divider2(25)); // Output: 5

// 7
function createShoppingList() {
    const list = [];
    return {
        addItem(item) {
            list.push(item);
        },
        removeItem(item) {
            const index = list.indexOf(item);
            if (index > -1) {
                list.splice(index, 1);
            }
        },
        getList() {
            return list;
        }
    };
}

const shoppingList1 = createShoppingList();
shoppingList1.addItem("Apples");
shoppingList1.addItem("Bananas");
console.log(shoppingList1.getList()); // Output: ["Apples", "Bananas"]
shoppingList1.removeItem("Apples");
console.log(shoppingList1.getList()); // Output: ["Bananas"]

// 8
function createStopwatch() {
    let startTime = null;
    return function() {
        if (!startTime) {
            startTime = Date.now();
            console.log("Stopwatch started.");
        } else {
            const elapsedTime = (Date.now() - startTime) / 1000;
            console.log(`Elapsed time: ${elapsedTime} seconds`);
        }
    };
}

const stopwatch1 = createStopwatch();
stopwatch1();
setTimeout(stopwatch1, 2000);