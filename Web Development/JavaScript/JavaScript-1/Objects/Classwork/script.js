// #1
let person = {};
person.name = "Om Patel";
person.age = 15;
person.city = "Stratford";

console.log(`Name: ${person.name}`);
console.log(`Age: ${person.age}`);
console.log(`City: ${person.city}`);

// #2
person.age = 16;
console.log(`Age: ${person.age}`);

// #3
let book = {};
book.title = "Atomic Habits";
book.author = "James Clear";
book.genre = "Self-help";

console.log("Author: ", book.author);
delete book.author;
console.log("Author: ", book.author);

// #4
let bookKeys = Object.keys(book);
console.log(bookKeys);

// #5
let bookValues = Object.values(book);
console.log(bookValues);

// #6
let bookEntries = Object.entries(book);
console.log(bookEntries);

// #7
const product = {
    name: "Wireless Mouse",
    price: 29.99,
    category: "Electronics"
};

console.log(`Product Name: ${product.name}`);
console.log(`Price: $${product.price}`);
console.log(`Category: ${product.category}`);

// #8
const stringifiedProduct = JSON.stringify(product);
console.log(stringifiedProduct);

// #9
// In HTML

// #10
const parsedProduct = JSON.parse(stringifiedProduct);

const productDetailsElement = document.getElementById('result');
productDetailsElement.innerHTML = `
<p><strong>Name:</strong> ${product.name}</p>
<p><strong>Price:</strong> ${product.price}</p>`;