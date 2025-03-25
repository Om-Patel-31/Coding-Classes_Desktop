// 4. and 5.
console.log("4. and 5.");
console.log("A: 6\nB: 2\nC: 1\nD: 5\nE: 3\nF: 4");

// 6.
console.log("6.");
function uploadImage(image, callback) {
    setTimeout(() => {
        callback(image);
    }, 4000);
}
uploadImage("image.jpg", (image) => {
    console.log(`Image ${image} uploaded`);
});

// 7.
console.log("7.");
function fetchData(url, callback) {
    setTimeout(() => {
        callback(`Data from ${url}`);
    }, 3000);
}
fetchData("https://www.google.com", (data) => {
    console.log(data);
});

// 8.
console.log("8.");
function processData(data, callback) {
    setTimeout(() => {
        callback(`Processed ${data}`);
    }, 2000);
}
processData("Data", (processedData) => {
    console.log(processedData);
});

// 9.
console.log("9.");
function performAction(action, callback){
    action = alert("Hi there!");
    setTimeout(() => {
        callback(`Action ${action} completed`);
    }, 1000);
}
performAction("Action", (action) => {
    console.log(action);
});

// 10.
console.log("10.");
function calculateTotal(items, callback) {
    for (let i = 0; i < items.length; i++) {
        setTimeout(() => {
            callback(items[i]);
        }, 0);
    }
    setTimeout(() => {
        callback(items[i]++);
    }, 2000);
}
calculateTotal([1, 2, 3, 4, 5], (total) => {
    console.log(total);
});

// 11.
console.log("11.");
function sendEmail(email, callback) {
    setTimeout(() => {
        callback(`Email sent to ${email}`);
    }, 4000);
}
sendEmail("[email protected]", (email) => {
    console.log(email);
});