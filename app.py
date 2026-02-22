"""Top-level launcher that proxies to backend/app.py.
This allows running `python app.py` from the workspace root as users expect.
"""

from backend.app import app

if __name__ == "__main__":
    # run with same settings as backend
    app.run(debug=True)
