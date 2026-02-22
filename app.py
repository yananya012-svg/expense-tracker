"""Top-level launcher that proxies to backend/app.py.
This allows running `python app.py` from the workspace root as users expect.
"""

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)

expenses = []

# ----------------------------
# MODEL TRAINING FUNCTION
# ----------------------------
def train_model():
    if len(expenses) < 3:
        return None

    df = pd.DataFrame(expenses)

    # Convert date to numeric day index
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df['day_number'] = (df['date'] - df['date'].min()).dt.days

    X = df[['day_number']]
    y = df['amount']

    model = LinearRegression()
    model.fit(X, y)

    return model, df


# ----------------------------
# ROUTES
# ----------------------------
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

        expenses.append({
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        })

        return redirect(url_for('expenses_list'))

    return render_template('add.html')


@app.route('/expenses')
def expenses_list():
    return render_template('expenses.html', expenses=expenses)


@app.route('/total')
def total_spending():
    total = sum(e['amount'] for e in expenses)
    return render_template('total.html', total=total)


@app.route('/predict')
def predict():
    # Prefer a saved model if available
    model = None
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
            use_saved = True
    except Exception:
        use_saved = False

    # If no saved model, train from current expenses
    if not use_saved:
        result = train_model()
        if result is None:
            return "Add at least 3 expenses to train the model or provide model.pkl."
        model, df = result
    else:
        # need dataframe to compute next day index
        if len(expenses) == 0:
            return "Add some expenses first."
        df = pd.DataFrame(expenses)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        df['day_number'] = (df['date'] - df['date'].min()).dt.days

    next_day = df['day_number'].max() + 1
    prediction = model.predict([[next_day]])[0]

    return render_template("predict.html", prediction=round(prediction, 2))


if __name__ == '__main__':
    app.run(debug=True)
