from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Medical Cost Prediction App Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([data])
    return f"Predicted Cost: {prediction[0]}"

if __name__ == "__main__":
    app.run(debug=True)