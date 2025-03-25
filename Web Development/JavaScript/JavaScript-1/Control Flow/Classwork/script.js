// #1
let isRaining = true;
if (isRaining == true){
    console.log("Take an umbrella.");
}
else{
    console.log("Leave the umbrella at home.");
}

// #2
let dayOfWeek = "Monday";
switch (dayOfWeek){
    case "Monday":
        console.log("Work.");
        break;
    case "Saturday":
        console.log("Relax.");
        break;
    default:
        console.log("Follow the routine.");
        break;
}

// #3
let age = 15;
if (age <= 18){
    console.log("You are an adult.");
}
else{
    console.log("You are not an adult.");
}

// #4
let trafficLight = "red";
switch (trafficLight) {
    case "red":
        console.log("Stop.");
        break;
    case "yellow":
        console.log("Slow down.");
        break;
    case "green":
        console.log("Go.");
        break;
    default:
        console.log("Invalid color.");
        break;
}

// #5
let count = 1;
while (count <= 10) {
    console.log(count);
    count++;
}

// #6
for (let i = 10; i >= 1; i--) {
    console.log(i);
}

// #7
let num = 1;
do {
    console.log(num);
    num++;
} while (num <= 5);

// #8
for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}

// #9
for (let i = 1; i <= 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}

// #10
let i = 1;
while (i <= 10) {
    if (i === 7) {
        i++;
        continue;
    }
    console.log(i);
    i++;
}

// #11
function calculateArea(width, height) {
    return width * height;
}

// #12
function findFactorial(n) {
    let factorial = 1;
    for (let i = 1; i <= n; i++) {
        factorial *= i;
    }
    return factorial;
}