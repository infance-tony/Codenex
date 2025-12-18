from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), 'atm.db')

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            amount REAL,
            date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    # Insert sample user
    cursor.execute("INSERT OR IGNORE INTO users (username, password, balance) VALUES (?, ?, ?)", ('user1', 'pass1', 1000.0))
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, balance FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user_id'] = user[0]
            session['balance'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    cursor.execute("SELECT type, amount, date FROM transactions WHERE user_id=? ORDER BY date DESC LIMIT 10", (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', balance=balance, transactions=transactions)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    amount = float(request.form['amount'])
    user_id = session['user_id']
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    if amount > balance:
        flash('Insufficient funds')
    else:
        new_balance = balance - amount
        cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user_id))
        cursor.execute("INSERT INTO transactions (user_id, type, amount, date) VALUES (?, ?, ?, ?)", (user_id, 'withdraw', amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        session['balance'] = new_balance
        flash('Withdrawal successful')
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/deposit', methods=['POST'])
def deposit():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    amount = float(request.form['amount'])
    user_id = session['user_id']
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    new_balance = balance + amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user_id))
    cursor.execute("INSERT INTO transactions (user_id, type, amount, date) VALUES (?, ?, ?, ?)", (user_id, 'deposit', amount, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    session['balance'] = new_balance
    flash('Deposit successful')
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)