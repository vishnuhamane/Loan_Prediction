from flask import Flask,render_template,request
import json
import numpy as np

with open('x_columns.json','r') as column_file:
    columns = json.load(column_file)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods =['POST'])
def loanapp():
    # columns = json.load('x_columns.json')
    data = np.zeros(len(columns))
    prop_type = request.form.get('property_type')

    print(columns)
    # if prop_type = 'Urban':
    #     data[index] = 1
    # prop_type = request.form.get('property_type')
    
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    # prop_type = request.form.get('property_type')
    
    
    return render_template('index.html')


if __name__=='__main__':

    app.run(debug=True,host='0.0.0.0',port=5000)