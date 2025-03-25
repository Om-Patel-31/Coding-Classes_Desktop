// 1.
import { EULER } from './geometryUtils.js'; 
const radiusCylinder = 4;
const heightCylinder = 8;
const volumeCylinder = EULER * radiusCylinder ** 2 * heightCylinder;
console.log(`${ volumeCylinder }`);

// 2.
import { reverseString } from "./textManipulator.js";
const str = "Hello, World!";
console.log(reverseString(str));

// 3.
import { calculateTotalCost, DISCOUNT_RATE } from "./shoppingCalculator.js";
const price = 25;
const quantity = 4;
const totalCost = calculateTotalCost(price, quantity);
const discountedTotalCost = totalCost * (1 - DISCOUNT_RATE / 100);
console.log(discountedTotalCost);

// 4.
// Completed in a different file

// 5.
// userName = "John";
// console.log(userName);
// Error: ReferenceError: userName is not defined

// 6.
// import { validate } from './strictValidationModule.js';
// console.log(validate(10)); 
// Uncaught ReferenceError: undeclaredVariable is not defined

// 7.
// Completed in a different file

// 8.
import { car } from './preferenceManager.js';
import { secretKey } from './secureModule.js';
car = prompt("What is your favorite car?");
console.log(car);

// 9.
console.log(secretKey); // This would throw an error if secretKey was not exported