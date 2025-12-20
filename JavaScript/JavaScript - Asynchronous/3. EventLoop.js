// Event Loop in JavaScript
// The event loop is a mechanism that handles asynchronous operations in JavaScript.
// It allows JavaScript to perform non-blocking I/O operations despite being single-threaded.
// The event loop continuously checks the call stack and the message queue (task queue).

// Example demonstrating the event loop:

console.log('1. Start of script'); // Synchronous, executed immediately

setTimeout(() => {
    console.log('3. Timeout callback'); // Asynchronous, added to task queue after 0ms
}, 0);

Promise.resolve().then(() => {
    console.log('2. Promise callback'); // Microtask, added to microtask queue
});

console.log('4. End of script'); // Synchronous, executed immediately

// How it works:
// 1. 'Start of script' is logged (call stack).
// 2. setTimeout schedules a callback in the task queue.
// 3. Promise.resolve().then schedules a microtask in the microtask queue.
// 4. 'End of script' is logged.
// 5. Call stack is empty, so microtasks are processed: 'Promise callback' is logged.
// 6. Then, tasks are processed: 'Timeout callback' is logged.
// Microtasks have higher priority than tasks.