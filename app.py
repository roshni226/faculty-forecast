from flask import Flask, request, jsonify,render_template
import pandas as pd
from model import ModelRun

# ModelRun()

app= Flask(__name__)

data = pd.read_csv("final.csv") 

@app.route('/templates/college_table.html')
def college():
    pivot_data = data.pivot_table(index=['RetirementYear', 'Designation'], columns='AreaOfSpecialization', aggfunc='size', fill_value=0)
    return render_template('college_table.html', table=pivot_data.to_html())

@app.route('/templates/vacancies_table.html')
def vacancies():
    grouped_data = data.groupby('RetirementYear').size().reset_index(name='total_vacancies')
    grouped_data['Faculty Recruitment'] = grouped_data['total_vacancies'].apply(lambda x: 'TWO PHASE' if 30<x<60 else ('THREE PHASE' if 60<=x<180 else ('FOUR PHASE' if 180<=x else('USUAL'))))
    return render_template('vacancies_table.html', table=grouped_data.to_html(index=False))

if __name__ == '__main__':
    app.run(debug=True,port = 5500)

 