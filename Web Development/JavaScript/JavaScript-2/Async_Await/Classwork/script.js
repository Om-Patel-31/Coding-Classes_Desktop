//4.
console.log("4.");
async function fetchUserData() {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}
fetchUserData();

//5.
console.log("5.");
async function processData(data) {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        data = await response.json();
        for (let i = 0; i < data.length; i++) {
            console.log(`\nName: ${data[i].name}`);
            console.log(`Username: ${data[i].username.toUpperCase()}`); 
        }
    } catch (error) {
        console.log(error);
    }
}
processData();

//6.
console.log("6.");
async function fetchAndProcessData() {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await response.json();
        for (let i = 0; i < data.length; i++) {
            console.log(`\nEmail: ${data[i].email}`);
            console.log(`Phone: ${data[i].phone}`);
        }
    } catch (error) {
        console.log(error);
    }
}
fetchAndProcessData();

//7.
console.log("7.");
async function fetchUserDetails() {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await response.json();
        for (let i = 0; i < data.length; i++) {
            console.log(`\nName: ${data[i].name}`);
            console.log(`Username: ${data[i].username.toUpperCase()}`);
            console.log(`Email: ${data[i].email}`);
            console.log(`Phone: ${data[i].phone}`);
        }
    } catch (error) {
        console.log(error);
    }
}
fetchUserDetails();

//8.
console.log("8.");
async function uploadFile() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("File Uploaded Successfully");
            resolve();
        }, 3000);
    });
}
uploadFile();

//9.
console.log("9.");
async function fetchWeatherForecast() {
    try{
        const response = await fetch('https://api.weatherapi.com/v1/current.json?key=edbefa48832c4f408e7204419251803&q=Canada&aqi=yes');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}
fetchWeatherForecast();

//10.
console.log("10.");
async function processUserInput(userName) {
    try{
        const response = await fetch(`https://jsonplaceholder.typicode.com/users?username=${userName}`);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}
username = prompt("Enter your name: ");
processUserInput(username);

//11.
console.log("11.");
async function fetchAndRenderData() {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await response.json();
        data.forEach(data => {
           data.name = data.name;
           data.username = data.username.toUpperCase();
           data.email = data.email;
           data.phone = data.phone;
        });
    }
    catch (error) {
        console.log(error);
    }
}
fetchAndRenderData();