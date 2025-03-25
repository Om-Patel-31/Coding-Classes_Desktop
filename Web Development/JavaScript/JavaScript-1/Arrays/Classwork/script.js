// #1
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

// #2
let numbers = [1, 2, 3, 4, 5];

// #3
let bonusNumbers = [6, 7, 8, 9, 10];
numbers.concat(bonusNumbers);

// #4
let fourthMonth = months[3];

// #5
months[6] = "July";

// #6
months.splice(2, 1);
console.log(months);

// #7
months.push("March");
console.log(months);

// #8
for (let month of months){
    console.log(month);
}

// #9
for (let month of months) {
    console.log(`${month}: ${month.length}`);
}

// #10
bonusNumbers.forEach((num, index, arr) => {
    arr[index] = num * 3;
});
console.log(bonusNumbers);

// #14
numbers.forEach(num => {
    console.log(num * num);
});

// #15
let abbreviatedMonths = [];
months.forEach(month => {
    abbreviatedMonths.push(month.slice(0, 3));
});
console.log(abbreviatedMonths);