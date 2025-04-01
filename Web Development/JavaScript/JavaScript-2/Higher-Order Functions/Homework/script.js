// 1.
function toUpperCaseArray(strings) {
    return strings.map(str => str.toUpperCase());
}

// 2.
function filterGreaterThanTen(numbers) {
    return numbers.filter(num => num <= 10);
}

// 3.
function calculateProduct(numbers) {
    return numbers.reduce((product, num) => product * num, 1);
}

// 4.
function calculateAverage(numbers) {
    const sum = numbers.reduce((total, num) => total + num, 0);
    return numbers.length > 0 ? sum / numbers.length : 0;
}

// 5.
function reverseStrings(strings) {
    return strings.map(str => str.split('').reverse().join(''));
}

// 6.
function toLowerCaseArray(strings) {
    return strings.map(str => str.toLowerCase());
}

// 7.
function concatenateStrings(strings) {
    return strings.reduce((result, str) => result + str, '');
}

// 8.
function appendDeveloperToNames(objects) {
    return objects.map(obj => `${obj.name} - Developer`);
}

// 9.
function filterNotDivisibleByThree(numbers) {
    return numbers.filter(num => num % 3 === 0);
}