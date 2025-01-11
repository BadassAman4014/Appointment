from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample appointments data
    appointments = [
        {"time": "09:00", "details": "Runny nose", "type": "sick"},
        {"time": "12:00", "details": "Keeping pregnant", "type": "checkup"},
        {"time": "12:30", "details": "Sprain", "type": "sick"},
        {"time": "13:00", "details": "Ultrasound", "type": "examination"},
        {"time": "13:30", "details": "ECG", "type": "examination"},
    ]
    return render_template('appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
