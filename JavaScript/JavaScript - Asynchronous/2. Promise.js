// Example of a Promise in JavaScript
// A Promise represents a value that may be available now, or in the future, or never.
// It has three states: pending, fulfilled (resolved), or rejected.

// Creating a Promise
const myPromise = new Promise((resolve, reject) => {
  // Simulate an asynchronous operation using setTimeout
  setTimeout(() => {
    const success = true; // Change to false to see rejection
    if (success) {
      resolve("Operation successful!"); // Fulfills the promise
    } else {
      reject("Operation failed!"); // Rejects the promise
    }
  }, 1000); // Waits 1 second
});

// Using the Promise
myPromise
  .then(result => {
    console.log("Success:", result); // Called if resolved
  })
  .catch(error => {
    console.log("Error:", error); // Called if rejected
  });

// Explanation:
// - Promise constructor takes a function with resolve and reject parameters.
// - resolve() changes state to fulfilled and passes the value.
// - reject() changes state to rejected and passes the error.
// - .then() handles the fulfilled case.
// - .catch() handles the rejected case.
// - Promises help manage asynchronous operations without callbacks.