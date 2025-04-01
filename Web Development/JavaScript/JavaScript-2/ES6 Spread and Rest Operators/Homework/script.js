// 1.
const sourceArray = [1, 2, 3, 4, 5];
const copyArray = [...sourceArray];
console.log(copyArray);

// 2.
const firstArray = [10, 20, 30];
const secondArray = [40, 50, 60];
const mergedArray = [...firstArray, ...secondArray];
console.log(mergedArray);

// 3.
const originalObj = { name: "John", age: 25 };
const clonedObj = { ...originalObj };
console.log(clonedObj);

// 4.
const objA = { a: 1, b: 2 };
const objB = { c: 3, d: 4 };
const resultObj = { ...objA, ...objB };
console.log(resultObj);

// 5.
const numbers = [100, 200, 300];
const info = { id: 1, status: "active" };
const combinedData = [...numbers, { ...info }];
console.log(combinedData);

// 6.
function calculateSum(...args) {
    return args.reduce((sum, num) => sum + num, 0);
}
console.log(calculateSum(1, 2, 3, 4, 5));

// 7.
function displayArgs(...args) {
    console.log(args);
}
displayArgs("Hello", "World", 123, true);

// 8.
function mergeArraysRecursive(...arrays) {
    return arrays.reduce((merged, array) => [...merged, ...array], []);
}
const arrayX = [1, 2];
const arrayY = [3, 4];
const arrayZ = [5, 6];
const mergedRecursiveArray = mergeArraysRecursive(arrayX, arrayY, arrayZ);
console.log(mergedRecursiveArray);