from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the saved model and scaler
model = pickle.load(open('restaurant_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get data from the HTML form
    # Note: You must collect Longitude, Latitude, Votes, Cost, Price Range
    votes = float(request.form['votes'])
    cost = float(request.form['cost'])
    # ... collect other inputs ...

    # 2. Apply the SAME transformations as the notebook
    log_votes = np.log1p(votes)
    
    # 3. Create a DataFrame for the scaler (needs to match training columns)
    # You will need to provide 0/1 for the City and Cuisine columns too!
    input_data = pd.DataFrame([[...]]) 
    scaled_data = scaler.transform(input_data)

    # 4. Predict
    prediction = model.predict(scaled_data)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Predicted Rating: {output}')

if __name__ == "__main__":
    app.run(debug=True)