// Example 1.
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(number => number * 2);
console.log(doubledNumbers);

// Example 2.
const names = ["alice", "bob", "charlie"];
const upperCasedNames = names.map(name => name.toUpperCase());
console.log(upperCasedNames);

// Example 3.
const evenNumbers = numbers.filter(number => number % 2 === 0);
console.log(evenNumbers);

// Example 4.
const words = ["apple", "banana", "orange", "blueberry"];
const filteredWords = words.filter(word =>
    word.startsWith("b"));
console.log(filteredWords);

// Example 5.
const sum = numbers.reduce((accumulator, currentValue) =>
    accumulator + currentValue, 0);
console.log(sum);

// Example 6.
const word = ["Hello", " ", "World", "!"];
const sentence = word.reduce((accumulator, currentValue) =>
    accumulator + currentValue, "");
console.log(sentence);