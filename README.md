# Expense Tracker

This repository contains a simple expense tracker application.

## Structure

```
expense-tracker/
│
├── app.py              # Flask web application
├── main.py             # CLI/terminal version
├── requirements.txt    # Dependencies
├── templates/          # HTML templates for the Flask app
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── expenses.html
│   └── total.html
```

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows PowerShell
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the web app

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser to use the web interface.

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