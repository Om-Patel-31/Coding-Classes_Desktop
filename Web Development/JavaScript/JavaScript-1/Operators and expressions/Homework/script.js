// #1
let originalPrice = 49.99;
let discount = 0.15 * originalPrice;
let discountedPrice = originalPrice - discount;
console.log(discountedPrice);

// #2
// 2. Toggle user's online status
let isOnline = true;
isOnline = !isOnline;
console.log(isOnline);

// 6. Consecutive withdrawals
let currentBalance = 500;
currentBalance -= 50;
console.log(currentBalance);
currentBalance -= 100;
console.log(currentBalance);
currentBalance -= 25;
console.log(currentBalance);

// 7. Concatenate product information
let product = {
    name: "Laptop",
    price: 999.99,
    category: "Electronics"
};
let productInfo = "Product: " + product.name + ", Price: $" + product.price + ", Category: " + product.category;
console.log(productInfo);

// 8. Check if userNumber is odd or even
let userNumber = 42;
let isEven = userNumber % 2 === 0;
console.log(userNumber + " is " + (isEven ? "even" : "odd"));

// 9. Calculate compound interest
let principalAmount = 1000;
let interestRate = 0.05;
let timeInYears = 5;
let finalAmount = principalAmount * (1 + interestRate) ** timeInYears;
console.log(finalAmount);

// 10. Equality comparison with type coercion
let num1 = 42;
let num2 = "42";
let isEqual = num1 == num2;
console.log(isEqual);

// 11. Check if user is of working age
let userAge = 30;
let isWorkingAge = userAge >= 18 && userAge <= 65;
console.log("User is of working age: " + isWorkingAge);

// 12. Update quantity and calculate total price
let initialQuantity = 20;
let pricePerUnit = 10;
initialQuantity += 5;
let totalPrice = initialQuantity * pricePerUnit;
console.log("Updated quantity: " + initialQuantity + ", Total price: $" + totalPrice);

// 13. Check if password is valid
let userPassword = "password123";
let secretPassword = "secret";
let isValidPassword = userPassword !== secretPassword;
console.log("Password is valid: " + isValidPassword);