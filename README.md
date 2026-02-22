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