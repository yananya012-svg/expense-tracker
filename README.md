# Expense Tracker

This repository contains a simple expense tracker application.

## Structure

```
expense-tracker/
│
├── backend/
│   ├── app.py            # Flask web application (backend)
│   └── requirements.txt  # Dependencies for backend
├── frontend/             # HTML templates and static frontend
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── expenses.html
│   └── total.html
├── main.py               # CLI/terminal version (left in root)
```

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows PowerShell
   ```
2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## Running the web app

You can start the server from either the backend folder or the project root:

```bash
# from backend folder
cd backend && python app.py

# or from the workspace root (launcher)
python app.py
```


Open `http://127.0.0.1:5000/` in your browser to use the web interface. **Do not try to open any HTML files directly using `file://` paths; you will see an "ERR_FILE_NOT_FOUND" message.**

## Using a saved model (`model.pkl`)

If you'd like the `/predict` route to use a pre-trained model instead of training on every request, place `model.pkl` in the project root. The app will attempt to load `model.pkl` first; if not found it will fall back to training a model from current expenses (requires at least 3 entries).

To create and save a model locally (example):

```python
import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd

# prepare df with 'date' and 'amount'
# df['date'] = pd.to_datetime(df['date'])
# df = df.sort_values('date')
# df['day_number'] = (df['date'] - df['date'].min()).dt.days

X = df[['day_number']]
y = df['amount']
model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
   pickle.dump(model, f)
```

Then restart the web app; `/predict` will use the saved model.

## Running the CLI app

```bash
python main.py
```

The CLI version runs in the terminal.

## Next steps

- Add a SQLite database instead of the in-memory store
- Improve UI with Bootstrap
- Deploy to a hosting service such as Heroku or PythonAnywhere

---

Feel free to fork and extend this project!