from flask import Flask, render_template, request, redirect
import sqlite3
import database
import tne

DB_PATH = database.initialize_database()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            percentage = float(request.form.get("percentage"))
        except ValueError:
            percentage = None
        try:
            rate = float(request.form.get("rate"))
        except ValueError:
            rate = None
        try:
            base = float(request.form.get("base"))
        except ValueError:
            base = None
        percentage, rate, base, percentageChange, percentIncrease, percentDecrease = tne.calcVal_bbm(percentage, rate, base, DB_PATH)
        try:
            database.updateBbm_db(percentage, rate, base, percentageChange, percentIncrease, percentDecrease, DB_PATH)
            return redirect('/')
        except:
            return "Invalid inputs or invalid values."
    else:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
        SELECT
            percentage,
            rate,
            base,
            percentageChange,
            percentIncrease,
            percentDecrease,
            created_at
        FROM bbm_db
        """)
        bbm_db = cursor.fetchall()
        conn.close()
        return render_template('index.html', bbm = bbm_db)        
if __name__ == '__main__':
    app.run(debug=True)
