console.log("Start");
setTimeout(() => {
    console.log("Async Task 1 (after 2 seconds)");
}, 2000);
console.log("Task 2");
console.log("End");

// Asynchronous function with a callback
function delayedGreet(name, callback) {
    setTimeout(() => {
        console.log(`Hello, ${name}!`);
        // Execute the callback function after a delay
        callback();
    }, 1000);
}
// Callback function
function sayGoodbye() {
    console.log("Goodbye!");
}
// Calling the asynchronous function with a callback
delayedGreet("Bob", sayGoodbye);

// Task A
function performTaskA(callbackA) {
    setTimeout(() => {
        console.log("Task A completed");
        callbackA();
    }, 1000);
}
// Task B (nested within Task A)
function performTaskB(callbackB) {
    setTimeout(() => {
        console.log("Task B completed");
        callbackB();
    }, 500);
}
// Initiating Task A
performTaskA(() => {
    // Task A completed, now initiate Task B
    performTaskB(() => {
        // Task B completed
        console.log("All tasks completed");
    });
});

function fetchData(callback) {
    // Simulating asynchronous operation (fetching data from a server)
    setTimeout(() => {
        const data = { message: "Hello, World!" };
        callback(data); // Execute the callback with the fetched data
    }, 2000);
}
function handleData(data) {
    console.log("Received data:", data.message);
}
// Calling fetchData with handleData as the callback
fetchData(handleData);