// Example of Callbacks in JavaScript

// A callback is a function passed as an argument to another function,
// which is then invoked inside the outer function to complete some kind of routine or action.

// Example: Simulating an asynchronous operation like fetching data

function fetchData(callback) {
    // Simulate a delay (e.g., network request)
    setTimeout(() => {
        const data = "Fetched data from server";
        callback(data); // Call the callback function with the data
    }, 2000); // 2 seconds delay
}

// Define a callback function
function displayData(data) {
    console.log("Data received:", data);
}

// Call fetchData with the callback
fetchData(displayData);

// Explanation:
// - fetchData is a function that takes a callback as a parameter.
// - Inside fetchData, after a simulated delay, it calls the callback with some data.
// - displayData is the callback function that handles the data (in this case, logs it).
// - This demonstrates asynchronous behavior where the callback is executed after the operation completes.