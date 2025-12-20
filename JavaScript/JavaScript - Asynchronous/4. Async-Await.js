// Async and Await in JavaScript
// Async functions allow you to write asynchronous code that looks synchronous.
// The 'async' keyword declares a function as asynchronous, which means it returns a Promise.
// The 'await' keyword pauses the execution of the async function until the Promise is resolved or rejected.

// Example: Simulating an asynchronous operation like fetching data from an API

// A function that simulates fetching data (returns a Promise)
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (Math.random() > 0.5) {
                resolve('Data fetched successfully!');
            } else {
                reject('Failed to fetch data!');
            }
        }, 2000); // Simulates a 2-second delay
    });
}

// An async function that uses await to handle the Promise
async function getData() {
    try {
        console.log('Fetching data...');
        const data = await fetchData(); // Waits for the Promise to resolve
        console.log(data); // Outputs: Data fetched successfully!
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the async function
getData();
