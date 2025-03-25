// #1
let isSunny = false;
if (isSunny == true){
    console.log("Wear sunglasses.");
}
else{
    console.log("No need for sunglasses.");
}

// #2
let month = "January";
switch (month){
    case "January":
    case "February":
    case "November":
    case "December":
        console.log("Season: Winter");
        break;
    case "March":
    case "April":
    case "May":
        console.log("Season: Spring");
        break;
    case "June":
    case "July":
    case "August":
        console.log("Season: Summer");
        break;
    case "September":
    case "October":
    case "November":
        console.log("Season: Fall");
        break;
    default:
        console.log("Enjoy without thinking of the weather.")
}

// #3
let grade = 91;
if (grade > 70){
    console.log("Pass");
}
else{
    console.log("Fail")
}

// #4
currentWeather = "sunny";
switch (currentWeather){
    case "sunny":
        console.log("Don't forget your sunglasses.");
        break;
    case "rainy":
        console.log("Don't forget your umbrella.");
        break;
    case "cloudy":
        console.log("Don't forget your coat.");
        break;
    default:
        console.log("Enjoy your day. Hope the weather outside is good.")
}

// #5
let i = 1;
while (i<7){
    console.log(i);
    i++;
}

// #6
for (i=5; i>0; i--){
    console.log(i);
}

// #7
i = 0
do{
    console.log(i);
    i++;
} while(i<4)

// #8
for (num=1; num<=15; num+=2){
    console.log(num);
}

// #9
for (let j=1; j<=6; j++) {
    if (j===3) {
        break;
    }
    console.log(j);
}

// #10
let a = 1;
while (a<=8){
    if (a===5){
        continue;
    }
    console.log(a);
}

// #11
function calculateVolume(radius, height){
    volume = radius*radius*height*Math.PI;
    return volume
}