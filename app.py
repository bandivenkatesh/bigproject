from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    birthdate_str = request.form['birthdate']
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.now()

    # Calculate age in years, months, and days
    delta = today - birthdate
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30

    return render_template('result.html', years=years, months=months, days=days)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

