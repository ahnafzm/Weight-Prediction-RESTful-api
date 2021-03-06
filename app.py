from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def Gender_prediction():
    if request.method == 'GET':
        return render_template("Weight-prediction.html")
    elif request.method == 'POST':
        print(dict(request.form))
        weight_features = dict(request.form).values()
        weight_features = np.array([float(x) for x in weight_features])
        model = joblib.load("model-development\Weight-Prediction-using-linear-regression.pkl")
        print(weight_features)
        result = model.predict([weight_features])
        return render_template('Weight-prediction.html', result=f"{int(result)} Kg")
    else:
        return "Unsupported Request Method"


if __name__ == '__main__':
    app.run(port=5000, debug=True)