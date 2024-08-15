from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('faculty_forecast.pkl')

# Define the columns that were used during training
training_columns = [
    'Age', 'JoiningYear', 'Gender_Male',
       'Designation_Associate Professor', 'Designation_Dean',
       'Designation_Director', 'Designation_Lecturer',
       'Designation_Research Professor', 'Designation_Senior Professor',
       'AreaOfSpecialization_Chemical Engineering',
       'AreaOfSpecialization_Civil Engineering',
       'AreaOfSpecialization_Computer Engineering',
       'AreaOfSpecialization_Data Science and Engineering',
       'AreaOfSpecialization_Electrical Engineering',
       'AreaOfSpecialization_Environmental Engineering',
       'AreaOfSpecialization_Geotechnical Engineering',
       'AreaOfSpecialization_Mechanical Engineering',
       'AreaOfSpecialization_Robotics and Automation',
       'AreaOfSpecialization_Software Engineering', 'AppointmentType_Conract',
       'AppointmentType_Regular'
]

# Define the month mapping
month_mapping = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
    'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

@app.route('/')
def home():
    return "Welcome to the Faculty Attrition Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Convert data to DataFrame
    df = pd.DataFrame([data])

    # Preprocess the input data (ensure it matches the training data format)
    df['EndMonth'] = df['EndMonth'].map(month_mapping)
    df['EndDate'] = pd.to_datetime(df['EndYear'].astype(str) + '-' + df['EndMonth'].astype(str) + '-01')
    df['StartDate'] = pd.to_datetime(df['JoiningYear'].astype(str) + '-01-01')
    df['DurationMonths'] = (df['EndDate'] - df['StartDate']).dt.total_seconds() / (30 * 24 * 60 * 60)

    # Drop unnecessary columns
    df = df.drop(columns=['EndYear', 'EndMonth', 'EndDate', 'StartDate', 'DurationMonths'])

    # Encode categorical variables
    df = pd.get_dummies(df, columns=['Gender', 'Designation', 'AreaOfSpecialization', 'AppointmentType'], drop_first=True)

    # Ensure the input data has the same columns as the training data
    for col in training_columns:
        if col not in df.columns:
            df[col] = 0
    df = df[training_columns]

    # Make predictions
    prediction = model.predict(df)

    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
