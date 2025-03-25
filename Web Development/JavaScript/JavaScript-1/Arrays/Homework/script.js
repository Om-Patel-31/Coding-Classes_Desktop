// #1
let countries = ["USA", "Canada", "Germany", "Australia", "Japan"];

// #2
let temperatures = [22, 25, 20, 18, 24, 27, 23];

// #3
let additionalTemps = [21, 26, 19, 22, 25, 28, 24];
let allTemperatures = temperatures.concat(additionalTemps);

// #4
console.log(countries[1]);

// #5
temperatures[3] = 30;

// #6
countries.shift();
console.log(countries);

// #7
countries.unshift("India");

// #8
temperatures.pop();
console.log(temperatures);

// #9
for (let country of countries) {
    console.log(country);
}

// #10
let totalTemperature = 0;
for (let temp of temperatures) {
    totalTemperature += temp;
}
let averageTemperature = totalTemperature / temperatures.length;
console.log(averageTemperature);

// #11
additionalTemps.forEach((temp, index, arr) => {
    arr[index] = temp * 2;
});
console.log(additionalTemps);

// #12
temperatures.forEach(temp => {
    let fahrenheit = (temp * 9/5) + 32;
    console.log(fahrenheit);
});