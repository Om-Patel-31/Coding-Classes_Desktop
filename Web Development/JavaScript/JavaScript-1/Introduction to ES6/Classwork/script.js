//#1
function nameFunction() {
    if (true) {
        let myAge = 15;
        console.log("My Age: "+myAge);
    }
    // console.log(localVar);
}
nameFunction();

//#2
const gravity = 9.8;
console.log(gravity);

//#3
const multiply = (x, y) => x*y;
console.log(multiply);

//#4
let userName = "John";
let welcomeMessage = `Hello, ${userName}! Welcome to the site.`;
console.log(welcomeMessage);

//#5
let month = "October";
let year = 2023;
let dateMessage = `Today is the ${month} of ${year}.`;
console.log(dateMessage);

//#6
let fruits = ["apple", "banana", "cherry"];
let [first, , last] = fruits;
console.log(first);
console.log(last);

//#7
let colors = ["red", "green", "blue", "yellow"];
let [primary, ...restColors] = colors;
console.log(restColors.length);

//#8
let book = {
    title: "To Kill a Mockingbird",
    author: "Harper Lee",
    pages: 281
};
let { title, author, pages } = book;
console.log(title, author, pages);

//#9
let personDetails = {
    // firstName: "Alice"
};
let { firstName = "John" } = personDetails;
console.log(firstName);