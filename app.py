from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model dari file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        features = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['blood_pressure']),
            float(request.form['skin_thickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            float(request.form['age']),
        ]
        data = np.array([features])
        result = model.predict(data)[0]
        prediction = "Positif Diabetes" if result == 1 else "Negatif Diabetes"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
