"""Top-level launcher that proxies to backend/app.py.
This allows running `python app.py` from the workspace root as users expect.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = float(request.form['amount'])

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses.append(expense)
        return redirect(url_for('expenses_list'))

    return render_template('add.html')

@app.route('/expenses')
def expenses_list():
    return render_template('expenses.html', expenses=expenses)

@app.route('/total')
def total_spending():
    total = sum(e['amount'] for e in expenses)
    return render_template('total.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
