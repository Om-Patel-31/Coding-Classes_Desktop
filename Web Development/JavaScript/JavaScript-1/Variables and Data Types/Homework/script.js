// 1. Practical Initialization
let currentTemperature = 25; // Replace 25 with the current temperature in your area
console.log(currentTemperature);

// 2. Variable Reassignment
let preferredLanguage = "JavaScript";
preferredLanguage = "Python";
console.log(preferredLanguage);

// 3. Using const for Constants
const MAX_SIZE = 100;
try {
    MAX_SIZE = 120; // This will throw an error
} catch (error) {
    console.log(error.message); // Output: Assignment to constant variable.
}

// 4. CamelCase Practice
let productName = "Laptop";
let productPrice = 999.99;
console.log(productName, productPrice);

// 5. Data Types and typeof Operator
let userStatus = true;
console.log(typeof userStatus); // Output: boolean

// 6. Objects and Methods
let product = {
    name: "Smartphone",
    price: 699.99,
    quantity: 2,
    calculateTotal: function() {
        return this.price * this.quantity;
    }
};
console.log(product);
console.log("Total cost:", product.calculateTotal());

// 7. Type Coercion with the - Operator
let itemName = "Apple";
let itemWeight = 5;
let result = itemName - itemWeight;
console.log(result); // Output: NaN (Not a Number)
// Explanation: Subtracting a number from a string results in NaN because the string cannot be coerced into a number for subtraction.

// 8. Type Coercion with the + Operator
let numberString = "10";
let numericValue = 5;
let sum = numberString + numericValue;
console.log(sum); // Output: "105"
// Explanation: The + operator concatenates the string and the number, resulting in a string "105".

// 9. Explicit Type Conversion
let isSunny = true;
let isSunnyString = String(isSunny);
console.log(isSunnyString); // Output: "true"
// Explanation: The boolean value true is explicitly converted to the string "true".