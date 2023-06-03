from flask import Flask, request, jsonify,render_template
import pandas as pd
from model import ModelRun

ModelRun()

app= Flask(__name__)

data = pd.read_csv("final.csv") 

pivot_data = data.pivot_table(index=['RetirementYear', 'Designation'], columns='AreaOfSpecialization', aggfunc='size', fill_value=0)

@app.route('/')
def index():
    return render_template('bootstrap_table.html', table=pivot_data.to_html(), )

if __name__ == '__main__':
    app.run(debug=True)

 