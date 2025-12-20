function foo(...args) {
    if (args.length === 1) {
        console.log(args[0]);
    } else if (args.length === 2) {
        console.log(args[0], args[1]);
    }
}

// Driver code
foo("Geeks")
foo("Geeks", "forGeeks");
foo("Geeks", "forGeeks", "Hello");
