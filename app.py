from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# in-memory store for expenses
expenses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # simple real value input page
    if request.method == 'POST':
        val_str = request.form.get('value')
        try:
            val = float(val_str)
        except (TypeError, ValueError):
            val = None
        return render_template('index.html', value=val)

    return render_template('index.html', value=None)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form.get('date')
        category = request.form.get('category')
        description = request.form.get('description')
        amount_str = request.form.get('amount')
        try:
            amount = float(amount_str)
        except (TypeError, ValueError):
            amount = 0.0

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount,
        }
        expenses.append(expense)
        return redirect(url_for('expenses_list'))

    return render_template('add.html')

@app.route('/expenses')
def expenses_list():
    return render_template('expenses.html', expenses=expenses)

@app.route('/total')
def total_spending():
    total = sum(item['amount'] for item in expenses)
    return render_template('total.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
