// Mouse Events
document.getElementById("myButton").addEventListener("click", 
    function() {
        console.log("Button clicked!");
    });

document.getElementById("myElement").addEventListener("dblclick",
    function() {
        console.log("Element double-clicked!");
    });

document.getElementById("myElement").addEventListener("mouseover",
    function() {
        console.log("Mouse over element!");
    });

// Keyboard Events
document.addEventListener("keypress", function(event) {
    console.log("Key pressed: " + event.key);
});

document.addEventListener("keydown", function(event) {
    console.log("Key pressed: " + event.key);
});

document.addEventListener("keyup", function(event) {
    console.log("Key released: " + event.key);
});

// Form Events
document.getElementById("myForm").addEventListener("submit",
    function(event) {
        event.preventDefault();
        console.log("Form submitted!");
});

document.getElementById("myInput").addEventListener("change",
    function() {
        console.log("Input value channged!");
});

document.getElementById("myInput").addEventListener("focus",
    function() {
        console.log("Input focused!");
});

document.getElementById("myInput").addEventListener("blur",
    function() {
        console.log("Input blurred!");
});

// Window Events
document.getElementById("myButton").addEventListener("load", function() {
        console.log("Page loaded!");
});

document.getElementById("myButton").addEventListener("resize", function() {
        console.log("Window resized!");
});

document.getElementById("myButton").addEventListener("scroll", function() {
        console.log("Window scrolled!");
});

// Custom Events
var customEvent = new CustomEvent("customEvent", {
    detail: {
        message: "Custom Event Triggered!"
    }
});

document.dispatchEvent(customEvent);

document.addEventListener("customEvent", function(event) {
    console.log(event.detail.message);
});

document.addEventListener("click", function(event) {
    console.log("Event type:", event.type);
    console.log("Target element:", event.target);
    console.log("Timestamp:", event.timeStamp);
    console.log("Mouse coordinates (X, Y):", event.clientX,
    event.clientY);
});