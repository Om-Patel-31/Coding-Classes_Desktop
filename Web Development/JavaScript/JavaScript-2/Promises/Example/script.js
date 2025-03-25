// Example: Simulating an asynchronous operation with a Promise
// Function to simulate a network request that resolves after a certain delay
function fetchData() {
  return new Promise((resolve, reject) => {
    // Simulate network delay with setTimeout
    setTimeout(() => {
      const success = Math.random() < 0.8; // 80% chance of
      success;
      if (success) {
        resolve("Data fetched successfully");
      } else {
        reject("Failed to fetch data");
      }
    }, 2000); // Simulate 2 seconds delay
  });
}
// Using the fetchData function
console.log("Fetching data...");
fetchData()
  .then((result) => {
    console.log("Data:", result); // Handle successful result
  })
  .catch((error) => {
    console.error("Error:", error); // Handle error
  });