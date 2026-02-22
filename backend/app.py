from flask import Flask, render_template, request, redirect, url_for

# point Flask to the frontend folder for templates
app = Flask(__name__, template_folder='../frontend')

# in-memory store for expenses
expenses = []

@app.route('/')
def index():
    return render_template('index.html')

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
