// 4. and 5.
console.log("#4 and #5");
console.log("A: 5");
console.log("B: 6");
console.log("C: 3");
console.log("D: 2");
console.log("E: 4");
console.log("F: 1");

// 6.
console.log("#6");
function downloadFile(url, callback) {
    setTimeout(() => {
        const message = `File downloaded from ${url}`;
        callback(message);
    }, 3000);
}

// 7.
console.log("#7");
let randomValue = Math.floor(Math.random() * 5000) + 1000;
function delayedAlert(message, callback) {
    setTimeout(() => {
        callback(message);
    }, randomValue);
}
delayedAlert("Alert 1!", console.log);
delayedAlert("Alert 2!", console.log);

// 8.
console.log("#8");
function someThing(x, callback) {
    console.log("Do something");
    callback();
}
someThing(1, function(){
    console.log("First anonymous callback!");
});

// 9.
console.log("#9");
function someThingElse(y, callback) {
    console.log("Do something else");
    callback();
}
someThingElse(2, function(){
    console.log("Second anonymous callback!");
});

// 10.
console.log("#10");
function doThirdThing(z, callback) {
    console.log("Do third thing");
    callback();
}
doThirdThing(3, function(){
    console.log("Third anonymous callback!");
});

// 11.
console.log("#11");
someThing(() => {
    console.log("First anonymous callback!");
    someThingElse(() => {
        console.log("Second anonymous callback!");
        doThirdThing(() => {
            console.log("Third anonymous callback!");
        });
    });
});