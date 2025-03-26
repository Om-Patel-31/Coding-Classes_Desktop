// 4.
console.log("4.");
const numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const doubledNumArray = numArray.map((num) => num * 2);
console.log(doubledNumArray);

// 5.
console.log("5.");
const filteredNumArray = numArray.filter((num) => num % 2 === 0);
console.log(filteredNumArray);

// 6.
console.log("6.");
const sumOfNumArray = numArray.reduce((accumulator, currentValue) => 
    accumulator + currentValue, 0);
console.log(sumOfNumArray);

// 7.
console.log("7.");
const wordsArray = ["hello", "world"];
const uppercaseWordsArray = wordsArray.map((word) => word.toUpperCase());
console.log(uppercaseWordsArray);

// 8.
console.log("8.");
const filteredWordsArray = wordsArray.filter((word) => word.length > 5);
console.log(filteredWordsArray);

// 9.
console.log("9.");
const sumOfWordsArray = wordsArray.reduce((accumulator, currentValue) =>
    accumulator + currentValue, "");
console.log(sumOfWordsArray);

// 10.
console.log("10.");
const students = {"Chris": 80, "David": 77, "Travis": 88, "Caleb": 95};
const averageGrade = Object.values(students).reduce((accumulator, currentValue) =>
    accumulator + currentValue, 0) / students.length;
console.log(averageGrade);

// 11.
console.log("11.");
const words = ["Hey", "there", "this", "is", "Javascript"];
const wordsObject = words.reduce((accumulator, currentValue) => {
    if (currentValue in accumulator) {
        accumulator[currentValue]++;
    }
    else {
        accumulator[currentValue] = 1;
    }
    return accumulator;
}, {});
console.log(wordsObject);

// 12.
console.log("12.");
const integers = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7];
const positiveIntegers = integers.filter((num) => num > 0);
console.log(positiveIntegers);