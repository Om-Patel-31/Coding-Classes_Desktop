//4.
console.log("#1");
const myPromise = new Promise((resolve, reject) => {
  resolve("Promise resolved successfully!");
});
console.log(myPromise);

//5.
console.log("#2");
const delayedPromise = new Promise((resolve) => {
  setTimeout(() => {
    resolve("Delayed Problem resolved");
  }, 3000);
});
console.log(delayedPromise);

//6.
console.log("#3");
const immediateRejectPromise = new Promise((reject) => {
  setTimeout(() => {
    reject("Promise rejected immediately");
  }, 0);
});
console.log(immediateRejectPromise);

//7.
console.log("#4");
function fetchDataPromise() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = Math.random() < 0.75;
      if (success) {
        resolve("Data successfully fetched");
      } else {
        reject("Failed to fetch data");
      }
    }, 2000);
  });
}
console.log("Fetching data...");
fetchDataPromise()
  .then((result) => {
    console.log("Data:", result);
  })
  .catch((error) => {
    console.log("Error:", error);
  });

//8.
console.log("#5");
myPromise
  .then((result) => {
    console.log("Result:", result);
  })
  .catch((error) => {
    console.log("Error:", error);
  });

//9.
console.log("#6");
delayedPromise
  .then((result) => {
    console.log("Result:", result);
  })
  .catch((error) => {
    console.log("Error:", error);
  });

//10.
console.log("#7");
immediateRejectPromise
  .then((result) => {
    console.log("Result:", result);
  })
  .catch((error) => {
    console.log("Error:", error);
  });