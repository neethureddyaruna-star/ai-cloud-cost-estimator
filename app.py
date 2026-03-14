from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Sample training data
X = np.array([
    [2,4,50,100],
    [4,8,100,200],
    [8,16,200,300],
    [16,32,500,500]
])

y = np.array([20,60,150,400])

model = LinearRegression()
model.fit(X,y)

@app.route('/')
def home():
    return "AI Cloud Cost Estimator Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    cpu = data['cpu']
    ram = data['ram']
    storage = data['storage']
    hours = data['hours']
    
    prediction = model.predict([[cpu,ram,storage,hours]])
    
    return jsonify({"Estimated Cost": float(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
