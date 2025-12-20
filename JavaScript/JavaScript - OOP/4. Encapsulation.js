function BankAccount(accountNumber, accountHolderName, balance) {
    let _accountNumber = accountNumber;
    let _accountHolderName = accountHolderName;
    let _balance = balance;

    function showAccountDetails() {
        console.log(`Account Number: ${_accountNumber}`);
        console.log(`Account Holder Name: ${_accountHolderName}`);
        console.log(`Balance: ${_balance}`);
    }

    function deposit(amount) {
        _balance += amount;
        showAccountDetails();
    }

    function withdraw(amount) {
        if (_balance >= amount) {
            _balance -= amount;
            showAccountDetails();
        } else {
            console.log("Insufficient Balance");
        }
    }

    return {
        deposit: deposit,
        withdraw: withdraw
    };
}

let myBankAccount = BankAccount("123456", "John Doe", 1000);

myBankAccount.deposit(500); 
// Output: Account Number: 123456 Account Holder Name: 
//John Doe Balance: 1500

myBankAccount.withdraw(2000); // Output: Insufficient Balance