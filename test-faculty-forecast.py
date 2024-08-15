import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'Age': 40,
    'JoiningYear': 2010,
    'EndYear': 2022,
    'EndMonth': 'June',  # Add this field since it's required
    'Gender': 'Male',
    'Designation': 'Associate Professor',
    'AreaOfSpecialization': 'Data Science and Engineering',
    'AppointmentType': 'Approve'
}

response = requests.post(url, json=data)
print(response.json())
